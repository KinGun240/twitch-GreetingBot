# userExpList
ユーザー、コメント数を保存しているファイルです。  
ほぼ全ての機能で使います。  
これらの値は、チャット欄にコメントが投稿された際に、自動で記録・更新されます。  
レベルはparam_greetingBot.pyのExpTableに応じてBotの起動時に書き換えるので、  
保存されている値は参照しません。  

## UserName
ユーザー名
## MessageCount
コメント数
## Level
レベル

# monsterList
モンスター名、ライフ、出現率を保存しているファイルです。  
Battleコマンドで使用します。  
ユーザーの攻撃力は[ユーザーのレベル]D6で計算されるので、  
ここからモンスターのライフを設定して下さい。  
モンスターの出現率は[各モンスターの出現率]/[全モンスターの出現率の合計値]で計算されます。  
従って、[25]と設定しても25[%]の確率で出現することにはなりません。  

## MonsterName
モンスター名
## Life
ライフ
## Appearance
出現率