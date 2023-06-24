# bot-discord-py

## example_bot.py

### 機能

* !hello で反応
* !embed でembedメッセージの例を送る
* ボイスチャンネルに入った状態で，!join !leaveで入退室
* ボイスチャンネルに入った状態で，!playで音声テスト再生

### 注意

* botのtokenを，developer portalから取得する
* developer portal のbotのせっていのところから，Privileged Gateway Intentsをオンにしておく

### ローカルで動かす

```
(venv) $ python example_bot.py
```

### replit + uptimerobot で動かす

つまづいたとこのみ書く
* .pyファイルをやや変更
```
import os
from keep_alive import keep_alive

TOKEN = os.environ['SECRET_DISCORD_TOKEN']
keep_alive()
try:
    client.run(TOKEN)
except:
    os.system("kill 1")
```

* keep_alive.py
```
from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
```

* replitのshellで以下
```
$ python3 -m pip install -U "discord.py[voice]"
$ ffmpeg --version

ここで謎のコードが走っている...
ffmpeg.binとなにかのどっちかをえらばされるので，前者を選択

ffmpeg: command not installed. Multiple versions of this command were found in Nix.
Select one to run (or press Ctrl-C to cancel):
Adding ffmpeg.bin to replit.nix
success
```
