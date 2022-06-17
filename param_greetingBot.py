# パラメーター項目 ###########################
# コメントログ保存の有無
IsSaveCommentsFile = False

# コメント反応の音声の有無
IsPlaySoundComment = True
# コメント反応の音声ファイル、WAVかMP3形式
CommentSound = 'metal03.wav'

# レベルアップコメントの有無
IsLevelupComment = True
# レベルアップコメントのBotメッセージ
# 例）LevelupMessage1 = 'さんは'
# 　　LevelupMessage2 = 'にレベルアップ！'
# 　　[Bot名]:[コメントしたユーザー] さんは[新しい数値]にレベルアップ！
LevelupMessage1 = 'さんのレベルが'
LevelupMessage2 = 'に上がりました！'
# レベルアップ時の音声の有無
IsPlaySoundLevelup = True
# レベルアップ時の音声ファイル、WAVかMP3形式
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

# 初回コメント挨拶の有無
IsGreetingComment = True
# 初回コメント挨拶のBotメッセージ
# 例）GreetingMessage = 'さん、ゆっくりしていってください。'
# 　　[Bot名]:[コメントしたユーザー] さん、ゆっくりしていってください。
GreetingMessage = 'さん、ようこそ！'
# 初回コメント挨拶の音声の有無
IsPlaySoundGreeting = True
# 初回コメント挨拶の音声ファイル、WAVかMP3形式
GreetingSound = 'tm2_chime002.wav'
