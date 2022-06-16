# 概要
Twitchのチャット欄のコメントに関連して様々なアクションを起こすbotです。  
音声はbotを起動しているPC上で鳴るので、必要に応じて配信に取り込むようにして下さい。  
* コメントされる度に、音声を鳴らせます。  
* 各視聴者のコメント数が一定以上に達したら、メッセージの書き込みと音声を鳴らせます。  
* bot起動後で各視聴者のコメントが初めての場合は、メッセージの書き込みと音声を鳴らせます。  

# 導入手順
0. Bot用Twitchアカウントを作成し、Oauthパスワードを取得します。  
1. [config.py]の＊＊＊＊＊となっている個所の情報を書き換えます。  
   それ以外の項目も、必要があれば書き換えてください。  
2. [sound]フォルダに、鳴らしたい音声ファイルを追加します(WAV、MP3形式)。  
   デフォルトで鳴らすファイルが入っているので、そのままでよければ変更不要です。  
3. [param_greetingBot.py]の各項目について、必要があれば書き替えてください。  
   特に、音声ファイルを変更する場合は、該当する箇所の書き換えが必要です。  
4. [GreetingBot.exe]を起動します。  

# 機能説明
* **コメントログ保存**  
  チャット欄のコメントを、CSVファイルに保存します。  
  ファイルへの保存については、[param_greetingBot.py]からON/OFFが可能です。  
  ※ログ保存ON/OFFの項目名:IsSaveCommentsFile デフォルトではFalse  
* **コメント反応**  
  チャット欄で視聴者がコメントする毎に、[param_greetingBot.py]で指定された音声を鳴らします。  
  音声については、[param_greetingBot.py]からON/OFFが可能です。  
  また、鳴らす音声ファイルについては、[param_greetingBot.py]から変更が可能です。  
  ※コメント反応用音声ON/OFFの項目名:IsPlaySoundComment デフォルトではTrue  
  ※コメント反応用音声ファイルの項目名:CommentSound デフォルトではmetal03.wav  
* **集計コメント反応**  
  各視聴者のコメント数を集計し、一定以上の数に達した場合に、  
  チャット欄でbotがメッセージを書き込み、[param_greetingBot.py]で指定された音声を鳴らします。  
  メッセージおよび音声のそれぞれで、[param_greetingBot.py]からON/OFFが可能です。
  また、鳴らす音声ファイルについては、[param_greetingBot.py]から変更が可能です。  
  さらに、メッセージ・効果音に必要なコメント数は、[param_greetingBot.py]で変更可能です。  
  ※集計コメント反応用メッセージON/OFFの項目名：IsLevelupComment デフォルトではTrue  
  ※集計コメント反応用音声ON/OFFの項目名:IsPlaySoundLevelup デフォルトではTrue  
  ※集計コメント反応用音声ファイルの項目名:LevelupSound デフォルトではtm2_power001.wav  
  ※集計コメント反応用必要コメント数の項目名:ExpTable  
* **初回コメント反応**  
  bot起動後の配信で、各視聴者のコメントが初めてである場合、  
  チャット欄でbotがメッセージを書き込み、[param_greetingBot.py]で指定された効果音を鳴らします。  
  2回目以降のコメントには実行しません。  
  メッセージおよび効果音のそれぞれで、[param_greetingBot.py]からON/OFFが可能です。  
  また、鳴らす音声ファイルについては、[param_greetingBot.py]から変更が可能です。  
  ※初回コメント反応用メッセージON/OFFの項目名:IsGreetingComment デフォルトではTrue  
  ※初回コメント反応用音声ON/OFFの項目名:IsPlaySoundGreeting デフォルトではTrue  
  ※初回コメント反応用音声ファイルの項目名:GreetingSound デフォルトではtm2_chime002.wav  

# 動作環境
* OS  
  Windows 10(64bit)でのみ動作確認しています。  
  MacOSへの対応予定は今のところないです。  

# 参考(config.pyの設定内容など)
* Twitchにチャット翻訳botを導入する  
  https://note.com/tatsuya_iwama/n/nc42feebbb53d
* 翻訳ちゃんFreeNextの導入・使用方法  
  https://croom.sytes.net/trans/
* TwitchIOでTwitchのBotを作る  
  https://qiita.com/maguro869/items/57b866779b665058cfe8

# ファイル構成
* GreetingBot.exe  
  本体となる実行ファイルです。無いと動きません。  
* GreetingBot.py  
  ソースコードです。無くても動きます。  
* config.py  
  設定ファイルです。動作に必要な設定です。  
* param_GreetingBot.py  
  パラメーターファイルです。挙動変更ための設定です。  
* Readme.md  
  説明書です。今読んでるコレ。  
* LICENSE  
  ライセンスを明記したファイルです。  
* [data]フォルダ  
  取得して保存するデータに関するファイルを置くフォルダです。  
  - userExpList.csv  
    各視聴者のコメント数を集計したファイルです。  
* [sound]フォルダ  
  音声ファイルを置くフォルダです。  
  - metal03.wav
  - tm2_chime002.wav
  - tm2_power001.wav

# その他
本ソフトウェアを利用した場合の一切の責任を私は負いません、よろしくお願いします。  
本ソフトウェアの使用時には、配信概要欄やら下記連絡先やらどっかに一言あると喜びます。  
* Mail  
  kingunsq@gmail.com
* Twitter  
  https://twitter.com/Kin_Gun_
* Github  
  https://github.com/KinGun240

# 履歴
## バージョン 1.1.3
 - 2022/06/16  
   取り急ぎ

## バージョン 1.1.2
 - 2022/06/16  
   config.pyと関連する項目名を変更

## バージョン 1.1.1
 - 2022/06/16  
   DebugがONになってたのを修正、メッセージ内容を調整  
   config.pyからCLIENT_IDの項目を削除、他微修正  
   Readme.mdをいろいろいっぱい修正  

## バージョン 1.1.0
 - 2022/06/14  
   レベルアップ機能を追加(画像とか動画とかどうやって出すんだろうか…？)  
   config.pyのいくつかの項目をparam_greetingBot.pyに移項  
   Readme.mdの誤記修正  

## バージョン 1.0.1
 - 2022/06/10  
   Debug周りの処理の不具合を修正  

## バージョン 1.0.0
 - 2022/05/31  
   1年以上放って置いてたのを掘り出してきた  

# License
The source code is licensed MIT.
