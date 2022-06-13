# パラメーター項目 ###########################
# コメントリストファイルの保存の有無
IsSaveCommentsFile = False
# コメント時の効果音の有無
IsPlaySoundComment = True
# コメント時の効果音、WAVかMP3のファイル
CommentSound = 'metal03.wav'

# レベルアップコメントの有無
IsLevelupComment = True
# レベルアップ時の効果音の有無
IsPlaySoundLevelup = True
# レベルアップ時の効果音、WAVかMP3のファイル
LevelupSound = 'tm2_power001.wav'
# 経験値テーブル
#  デフォルト(Level n - 必要な経験値)
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

# 挨拶コメントの有無
IsGreetingComment = True
# 挨拶コメント時の効果音の有無
IsPlaySoundGreeting = True
# 挨拶コメント時の効果音、WAVかMP3のファイル
GreetingSound = 'tm2_chime002.wav'
