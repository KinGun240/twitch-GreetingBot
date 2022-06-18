# パラメーター項目 ###########################
# コメントログ保存のON/OFF
IsSaveCommentsFile = False

# 無視ユーザーリスト
IgnoreUsersList = ['Nightbot', 'StreamElements', 'moobot']
# 無視テキストリスト
IgnoreTextList = ['http']

# コメント反応の音声のON/OFF
IsPlaySoundComment = True
# コメント反応の音声ファイル、WAVかMP3形式
# ファイルは[sound]フォルダに置いてください
CommentSound = 'metal03.wav'

# レベルアップコメントのON/OFF
IsLevelupComment = True
# レベルアップコメントのBotメッセージ内容
# 例）LevelupMessage1 = 'さんはコメントによる経験を得て'
# 　　LevelupMessage2 = 'にレベルアップ！'
# 　　[Bot名]:[コメントしたユーザー] さんはコメントによる経験を得て[新しい数値]にレベルアップ！
LevelupMessage1 = 'さんは今のコメントにより、レベルが'
LevelupMessage2 = 'に上がりました！'
# レベルアップ時の音声のON/OFF
IsPlaySoundLevelup = True
# レベルアップ時の音声ファイル、WAVかMP3形式
# ファイルは[sound]フォルダに置いてください
LevelupSound = 'tm2_power001.wav'
# コメント数テーブル
#  デフォルト(Level n - 必要なコメント数)
#  Level 1 - 2
#  Level 2 - 4
#  Level 3 - 8
#  Level 4 - 16
#  Level 5 - 32
#  Level 6 - 64
#  Level 7 - 128
#  Level 8 - 256
#  Level 9 - 512
#  Level 10 - 999
ExpTable = [(2**1), (2**2), (2**3), (2**4), (2**5), (2**6), (2**7), (2**8),
            (2**9), 999]

# 初回コメント挨拶のON/OFF
IsGreetingComment = True
# 初回コメント挨拶のBotメッセージ内容
# 例）GreetingMessage = 'さん、ゆっくりしていってください。'
# 　　[Bot名]:[コメントしたユーザー] さん、ゆっくりしていってください。
GreetingMessage = 'さん、ようこそ！'
# 初回コメント挨拶の音声のON/OFF
IsPlaySoundGreeting = True
# 初回コメント挨拶の音声ファイル、WAVかMP3形式
# ファイルは[sound]フォルダに置いてください
GreetingSound = 'tm2_chime002.wav'

# コマンドパラメーター項目 ###########################
# expコマンドのON/OFF
IsExpCommand = True

# levelコマンドのON/OFF
IsLevelCommand = True

# nextコマンドのON/OFF
IsNextCommand = True
