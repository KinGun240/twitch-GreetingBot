# 概要
Twitchのチャット欄に指定のコマンドを入力することによって、  
起動中のOBSを操作するbotを出現させるソフトです。

# 使い方
※1.は初回のみ、2. 3.は必要に応じて実施
1. [obs-websocket]をインストールし、OBS Studioに適用します  
   ※2022/05/26現在の最新の安定板↓  
    https://github.com/obsproject/obs-websocket/releases/tag/4.9.1
2. OBS Studioの「ツール」「WebSocketサーバー設定」から、以下の設定を有効にします
 + 「WebSocketsサーバーを有効にする」にチェックを入れる
 + 「サーバーポート」に任意の数字を入力する(デフォルト:4444)
 + 「認証を有効にする」にチェックを入れる
 + 「パスワード」に任意の文字列を入力する
3. [config.py]および[param_commandsBot.py]に必要な情報を入力します  
   特に[config.py]で'----------'となっている個所は必ず設定してください  
   [param_commandsBot.p]で"----------"となっている箇所も設定してください
4. OBS Studioを起動します
5. [Commandsbot.exe]を起動します

# コマンド説明
## 実装コマンド(XXは01から始まる数字、現在は02まで)
 - **hello**
    挨拶を返す
 - **bot**
    実装されているコマンド一覧
 - **sceneXX**
    シーンを変更するコマンド
 - **volXX**
    ソースの音量を変更するコマンド
 - **moveXX**
    ソースを移動・拡大縮小するコマンド
 - **onoffXX**
    ソースをＯＮ／ＯＦＦするコマンド

## コマンド詳細
 - **sceneXX**
    + コマンドフォーマット  
     [BOT_PREFIX]sceneXX
    + コマンド例  
     !scene01
 - **volXX**
    + コマンドフォーマット  
     [BOT_PREFIX]volXX [音量:0~1000までの数値][%]
    + コマンド例  
     !vol01 50
 - **moveXX**
    + コマンドフォーマット  
     [BOT_PREFIX]moveXX [x方向位置:正の整数][px] [y方向位置:正の整数][px] [x方向縮尺率:実数][%] [y方向縮尺率:実数][%] [回転角度:実数][deg]  
     ※x方向縮尺率、y方向縮尺率、回転角度は省略可能
    + コマンド例  
     !move01 100 100
 - **onoffXX**
    + コマンドフォーマット  
     [BOT_PREFIX]onoffXX [ON/OFF:'ON'または'OFF'][-]
    + コマンド例  
     !onoff01 ON

# 動作環境
* OS  
  Windows 10でのみ動作確認しています  
  MacOSは対応予定は今のところないです
* OBS  
  OBS Studioでのみ動作確認しています

# 参考(config.py設定内容)
* TwitchIOでTwitchのBotを作る  
  https://qiita.com/maguro869/items/57b866779b665058cfe8

* 動画配信ソフト「OBS」をPythonで操るぞ～  
  https://techblog.kayac.com/2018/12/24/090000

# その他
本ソフトウェアを利用した場合の一切の責任を私は負いません、よろしくお願いします  
使用時には、どっかに一言頂けると喜びます  
* 連絡先  
  kingunsq@gmail.com
* Twitter  
  https://twitter.com/Kin_Gun_
* Github  
  https://github.com/KinGun240

# 履歴
## バージョン 1.0.0
 - 2022/05/29  
   とりあえずそれっぽい感じで作成
