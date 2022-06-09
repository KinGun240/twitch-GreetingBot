# 概要
Twitchのチャット欄にコメントされる度に音声を鳴らし、  
その配信中で初めてのコメントの場合は歓迎用の音声を鳴らすbotを出現させるソフトです。

# 使い方
※1.2.は必要に応じて実施  
1. [config.py]に必要な情報を入力します  
   特に'----------'となっている個所は必ず設定してください  
2. [sound]フォルダに、鳴らしたい音声ファイルを追加します(WAVファイル)  
   デフォルトで鳴らすファイルが入っているので、そのままでよければ変更不要です
3. OBS Studioを起動します
4. [Commandsbot.exe]を起動します

# 機能説明
* **初回コメント時挨拶**  
  bot起動後から初めてコメントする際、チャット欄でbotが挨拶コメントを返し、  
  [config.py]で指定された効果音を鳴らします  
  2回目以降のコメントには実施しません  
  挨拶コメントおよび効果音のそれぞれで、[config.py]からON/OFFが可能です
* **コメント時効果音**  
  チャット欄でコメントされる毎に、[config.py]で指定された効果音を鳴らします
  効果音について、[config.py]からON/OFFが可能です
* **コメントログ保存**  
  チャット欄のコメントをCSVファイルに保存します
  ファイルへの保存について、[config.py]からON/OFFが可能です

# 動作環境
* OS  
  Windows 10でのみ動作確認しています  
  MacOSは対応予定は今のところないです

# 参考(config.py設定内容)
* TwitchIOでTwitchのBotを作る  
  https://qiita.com/maguro869/items/57b866779b665058cfe8

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
## バージョン 1.0.1
 - 2022/06/10  
   Debug周りの処理の不具合を修正

## バージョン 1.0.0
 - 2022/05/31  
   1年以上放って置いてたのを掘り出してきた

# License
The source code is licensed MIT.
