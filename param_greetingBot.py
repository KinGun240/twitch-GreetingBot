# パラメーター項目 ###########################
# 音声・効果音ファイルは、WAVかMP3形式のみ対応しています。ファイルは[sound]フォルダに置いてください。
# 音声・効果音のボリュームは、0~100の範囲で指定して下さい。

# 無視ユーザーリスト
IgnoreUsersList = ['Nightbot', 'StreamElements', 'moobot']
# 無視テキストリスト
IgnoreTextList = ['http']

# コメントログ保存のON/OFF
IsSaveCommentsFile = False

# コメント反応の音声のON/OFF
IsPlaySoundComment = True
# コメント反応の音声ファイル
CommentSound = 'metal03.wav'
# コメント反応の音声のボリューム
CommentVolume = 100

# レベルアップコメントのON/OFF
IsLevelupComment = True
# レベルアップコメントのBotメッセージ内容
# [Bot名]:[コメントしたユーザー] LevelupMessage1[新しい数値]LevelupMessage2
# 例）LevelupMessage1 = 'さんはコメントによる経験を得て'
# 　　LevelupMessage2 = 'にレベルアップ！'
# 　　[Bot名]:[コメントしたユーザー] さんはコメントによる経験を得て[新しい数値]にレベルアップ！
LevelupMessage1 = 'さんは今のコメントにより、レベルが'
LevelupMessage2 = 'に上がりました！'
# レベルアップ時の音声のON/OFF
IsPlaySoundLevelup = True
# レベルアップ時の音声ファイル
LevelupSound = 'tm2_power001.wav'
# レベルアップ時の音声の音声のボリューム
LevelupVolume = 100
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
# [Bot名]:[コメントしたユーザー] GreetingMessage
# 例）GreetingMessage = 'さん、ゆっくりしていってください。'
# 　　[Bot名]:[コメントしたユーザー] さん、ゆっくりしていってください。
GreetingMessage = 'さん、ようこそ！'
# 初回コメント挨拶の音声のON/OFF
IsPlaySoundGreeting = True
# 初回コメント挨拶の音声ファイル
GreetingSound = 'tm2_chime002.wav'
# 初回コメント挨拶の音声のボリューム
GreetingVolume = 100

# コマンドパラメーター項目 ###########################
# expコマンドのON/OFF
IsExpCommand = True

# levelコマンドのON/OFF
IsLevelCommand = True

# nextコマンドのON/OFF
IsNextCommand = True

# battleコマンドのON/OFF
IsBattleCommand = True
# battleによるモンスター出現時の音声のON/OFF
IsPlaySoundBattleEncounter = True
# battleによるモンスター出現時の音声ファイル
BattleEncounterSound = 'tm2_bush001.wav'
# battleによるモンスター出現時の音声のボリューム
BattleEncounterVolume = 80
# battleによる勝利時の音声ファイル
BattleWinSound = 'tm2_quiz000good.wav'
# battleによる勝利時の音声のボリューム
BattleWinVolume = 100
# battleによる敗北時の音声ファイル
BattleLoseSound = 'tm2_quiz002bad.wav'
# battleによる敗北時の音声のボリューム
BattleLoseVolume = 100
