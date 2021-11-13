# 楽天競馬自動入金ツール

楽天競馬に毎日入金するのを自動化しました。<br>
**[Qiita](https://qiita.com/wadakatu/items/867640340564e571e8f7)**

## 使い方

### 1. ソースコードをクローン

```
git clone https://github.com/wadakatu/rakuten_horse.git
```

### 2. ChromeDriverをインストール

下記URLから、あなたが使用しているGoogle Chromeのバージョンと一致する<br>
ChromeDriverをインストールしてください。<br>

https://chromedriver.chromium.org/downloads

インストールした後は、クローンしたソースコード群と同階層に移動させてください。<br>
そして、main.pyを開いて、下記コードにChromeDriverのパスを入力してください。

```
 # webdriver準備
 driver = webdriver.Chrome("ChromeDriverのパス")
```

### 3. クレデンシャル情報設定

config.pyを開いて、各種クレデンシャル情報を入力してください。<br>
Slack系に関しては、入力しても入力しなくても大丈夫です。<br>
Slackアプリ設定方法は[こちら](https://api.slack.com/messaging/webhooks)

```
CONFIG = {
    'mailAddress': 'test@gmail.com',　#ログインメールアドレス
    'password': 'test_password',　#ログインパスワード 
    'pinCode': 1111, #楽天銀行のPIN番号
    'amountOfMoney': 100, #入金金額
    'slack': 'https://hooks.slack.com/services/test_token', #Incoming WebhookのURL
    'slackUser': '12345ABCDE' #DM送信先のユーザーID（slack）
}
```

### 4. 準備完了！

これで、スクリプトの準備が完了しました。
下記コマンドを入力すれば、自動入金作業が動作するはずです。

```
python3 main.py
```

### ※ヘッドレスモード

初期状態では、スクリプトを起動するたびに、Google Chromeが起動します。<br>
もし、ヘッドレスモードで起動したい場合は、main.pyに下記を追加してください。

```
 # webdriver準備(ヘッドレスモードの場合はoptions=optionsを追加）
 driver = webdriver.Chrome("./chromedriver", options=options)
```
