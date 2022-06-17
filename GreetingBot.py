# Copyright 2022 KinGun
# This software is released under the MIT License, see LICENSE.

from twitchio.ext import commands
from playsound import playsound

from shutil import rmtree
import os
import glob
import csv
import importlib
import pandas as pd
import sys
import signal
import unicodedata

Debug = False

# バージョン
ver = '1.2.0'

# 固定値
CommentLogFile = "commentLog.csv"
UserExpFile = "userExpList.csv"
ErrorLogFile = 'errorLog.csv'

# 各種初期設定 #####################################
# bot用コンフィグの読み込み
try:
    sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
    configGreeting = importlib.import_module('config')
    print("Read config.py")
    # remove "#" mark ------
    if configGreeting.Twitch_Channel.startswith('#'):
        print("Find # mark at channel name! I remove '#' from 'config:Twitch_Channel'")
        configGreeting.Twitch_Channel = configGreeting.Twitch_Channel[1:]
    # remove "oauth:" mark ------
    if configGreeting.Bot_OAUTH.startswith('oauth:'):
        print("Find 'oauth:' at OAUTH text! I remove 'oauth:' from 'config:Bot_OAUTH'")
        configGreeting.Bot_OAUTH = configGreeting.Bot_OAUTH[6:]
except Exception as e:
    print(e)
    print('Please make [config.py] and put it with GreetingBot')
    input()  # stop for error!!

# botの初期化
try:
    bot = commands.Bot(
        irc_token="oauth:" + configGreeting.Bot_OAUTH,
        client_id="",
        nick=configGreeting.Bot_ChannelName,
        prefix=configGreeting.BOT_PREFIX,
        initial_channels=[configGreeting.Twitch_Channel]
    )
except Exception as e:
    print(e)
    print('Please check [config.py]')
    input()  # stop for error!!

# GreetingBot用パラメーターの読み込み
try:
    greetingParam = importlib.import_module('param_greetingBot')
    print("Read param_greetingBot.py")
except Exception as e:
    print(e)
    print('Please make [param_greetingBot.py] and put it with GreetingBot')
    input()  # stop for error!!


# 内部変数の設定 ----------
# ユーザー経験値リストの読み込み
try:
    UserExpList = pd.read_csv(f"./data/{UserExpFile}")
    print(f"Read {UserExpFile}")
except Exception as e:
    print(e)
    print(f'Please check [{UserExpFile}] and put it with data folder')
    input()
if Debug:
    print(UserExpList)

# ユーザーメッセージ数リストにコメント数テーブルに基づいたレベルを設定
try:
    UserExpList['Level'] = 0
    for index, row in UserExpList.iterrows():
        for stepIndex, stepNum in enumerate(greetingParam.ExpTable):
            if row.MessageCount < stepNum:
                UserExpList.at[index, 'Level'] = int(stepIndex)
                break
except Exception as e:
    print(e)
    print('Please check [param_greetingBot.py] and put it with GreetingBot')
    input()
if Debug:
    print(UserExpList)

# 初見ユーザーリストの初期化
FirstUserList = []
# FirstUserList = [str.lower() for str in FirstUserList]


# bot処理 #####################################
# bot起動時処理 ----------
@bot.event
async def event_ready():
    print(f"{configGreeting.Bot_ChannelName}がオンラインになりました!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(configGreeting.Twitch_Channel,
                          f"/color {configGreeting.TextColor}")
    await ws.send_privmsg(configGreeting.Twitch_Channel,
                          "/me has landed! Hello!!")

    # 書き込み開始のファイル出力
    if greetingParam.IsSaveCommentsFile:
        with open(CommentLogFile, 'a') as commentsFile:
            writer = csv.writer(commentsFile)
            writer.writerow(['#Start Write Comments'])
            commentsFile.close()
        print(f'{CommentLogFile}にコメント保存を開始します')


# メッセージ受信時処理 ----------
@bot.event
async def event_message(ctx):
    onComment = False
    onLevelup = False
    onFirstMsg = False
    user = ctx.author.name.lower()
    name = ctx.author.display_name
    msg = ctx.content
    time = (pd.Timestamp(ctx.timestamp, unit='s', tz='UTC')
            ).tz_convert('Asia/Tokyo')
    # isMod = ctx.author.is_mod
    # is_Sub = ctx.author.is_subscriber

    if Debug:
        print(f'echo: {ctx.echo}, {msg}')
    # メッセージがコマンドまたはbotの投稿の場合は処理終了
    await bot.handle_commands(ctx)
    if not Debug:
        if ctx.content.startswith('!') or ctx.echo or user == bot.nick:
            return
    print(f'\nTIME:{time}\nUSER:{user}\nMSG:{msg}')

    # コメント反応処理 ----------
    # コメント反応のフラグ処理
    if greetingParam.IsPlaySoundComment:
        onComment = True

    # 集計コメント反応処理 ----------
    global UserExpList
    key = 'UserName'
    value = 'MessageCount'
    # ユーザーがユーザーメッセージ数リストに存在する場合はMessageCountを１追加
    # 存在しない場合はユーザーメッセージ数リストに追加
    count = 1
    try:
        row = UserExpList.query(f"{key} in ['{user}']")
        if not row.empty:
            count = row[value] + 1
            UserExpList.loc[UserExpList[key] == user, value] = count
        else:
            newRow = pd.DataFrame([[user, count]], columns=[key, value])
            UserExpList = UserExpList.append(newRow, ignore_index=True)
    except Exception as e:
        print('error: UserExpList not read...')
        if Debug:
            print(e.args)

    # ユーザーのメッセージ数に応じてレベルアップさせる
    try:
        oldLevel = UserExpList.loc[UserExpList[key] == user, 'Level'].item()
        newLevel = 0
        row = UserExpList.query(f"{key} in ['{user}']")
        for stepIndex, stepNum in enumerate(greetingParam.ExpTable):
            if row[value].item() < stepNum:
                newLevel = stepIndex
                UserExpList.loc[UserExpList[key] ==
                                user, 'Level'] = int(newLevel)
                break
    except Exception as e:
        print('error: UserExpList not read...')
        if Debug:
            print(e.args)
    print(UserExpList)

    # レベルアップのフラグ処理
    if newLevel > oldLevel:
        onLevelup = True

    # 初回コメント挨拶処理 ----------
    global FirstUserList
    # ユーザーが初見ユーザーリストに存在しない場合は初見ユーザーリストへ追加
    # かつ初見コメント挨拶のフラグ処理
    if user not in FirstUserList:
        FirstUserList.append(user)
        onFirstMsg = True
    print(f'FirstUserList:{FirstUserList}')

    # 音声・メッセージ処理 ----------
    # 各フラグ状態に応じてメッセージ出力
    try:
        if onFirstMsg and greetingParam.IsGreetingComment:
            out_text = f'{name} ' + greetingParam.GreetingMessage
            await ctx.channel.send("/me " + out_text)
            print(f'BotMessage:{out_text}')

        if onLevelup and greetingParam.IsLevelupComment:
            out_text = f'{name} ' + greetingParam.LevelupMessage1 + \
                f'{newLevel}' + greetingParam.LevelupMessage2
            await ctx.channel.send("/me " + out_text)
            print(f'BotMessage:{out_text}')
    except Exception as e:
        print('message send error')
        if Debug:
            print(e.args)

    # 各フラグ状態に応じて音声出力
    try:
        if onFirstMsg and greetingParam.IsPlaySoundGreeting:
            playsound(f"./sound/{greetingParam.GreetingSound}", True)
            print(f'BotSound:{greetingParam.GreetingSound}')
        elif onComment:
            playsound(f"./sound/{greetingParam.CommentSound}", True)
            print(f'BotSound:{greetingParam.CommentSound}')

        if onLevelup and greetingParam.IsPlaySoundLevelup:
            playsound(f"./sound/{greetingParam.LevelupSound}", True)
            print(f'BotSound:{greetingParam.LevelupSound}')
    except Exception as e:
        print('sound error: Please check [config.py] and sound folder...')
        if Debug:
            print(e.args)

    # その他処理 ----------
    # コメントログ保存処理:タイムスタンプ、ユーザー名、コメント内容
    try:
        if greetingParam.IsSaveCommentsFile:
            with open(CommentLogFile, 'a') as commentsFile:
                writer = csv.writer(commentsFile)
                writer.writerow([time, user, msg])
                commentsFile.close()
    except Exception as e:
        print(f'file error: [{CommentLogFile}] can not save...')
        if Debug:
            print(e.args)

    # ユーザーメッセージ数リストを保存しなおす
    try:
        UserExpList.to_csv(f"data/{UserExpFile}", index=False)
    except Exception as e:
        print(f'file error: [{UserExpFile}] can not save...')
        if Debug:
            print(e.args)


#####################################
# マルチバイト文字を判別して文字列の長さを返す処理 -------------
def count_text(message):
    # 文字列長カウント用の変数を定義
    text_length = 0
    # 文章中の文字数分ループを回す
    for i in message:
        letter = unicodedata.east_asian_width(i)
        # print(letter)
        if letter == 'H':       # 半角
            text_length = text_length + 1
        elif letter == 'Na':    # 半角
            text_length = text_length + 1
        elif letter == 'F':     # 全角
            text_length = text_length + 2
        elif letter == 'A':     # 全角
            text_length = text_length + 2
        elif letter == 'W':     # 全角
            text_length = text_length + 2
        else:                   # 半角
            text_length = text_length + 1
    return text_length


#####################################
# 最後のクリーンアップ処理 -------------
def cleanup():
    print("!!!Clean up!!!")

    # Cleanup処理いろいろ

    # time.sleep(1)
    print("!!!Clean up Done!!!")


#####################################
# sig handler  -------------
def sig_handler(signum, frame) -> None:
    sys.exit(1)


#####################################
# _MEI cleaner  -------------
# Thanks to Sadra Heydari
# @ https://stackoverflow.com/questions/57261199/
#   python-handling-the-meipass-folder-in-temporary-folder
def CLEANMEIFOLDERS():
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.abspath(".")

    if Debug:
        print(f'_MEI base path: {base_path}')
    base_path = base_path.split("\\")
    base_path.pop(-1)
    temp_path = ""
    for item in base_path:
        temp_path = temp_path + item + "\\"

    mei_folders = [f for f in glob.glob(temp_path + "**/", recursive=False)]
    for item in mei_folders:
        if item.find('_MEI') != -1 and item != sys._MEIPASS + "\\":
            rmtree(item)


# メイン処理 ###########################
def main():
    signal.signal(signal.SIGTERM, sig_handler)

    try:
        # 以前に生成された _MEI フォルダを削除する
        CLEANMEIFOLDERS()

        # bot
        bot.run()

    except Exception as e:
        if Debug:
            print(e)
        input()  # stop for error!!

    finally:
        signal.signal(signal.SIGTERM, signal.SIG_IGN)
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        cleanup()
        signal.signal(signal.SIGTERM, signal.SIG_DFL)
        signal.signal(signal.SIGINT, signal.SIG_DFL)


if __name__ == "__main__":
    sys.exit(main())
