# 権限が必要なgoogle fomesスクレイピング　非推奨
## chrome profile
アクセスするアカウントのプロファイルを探す
デフォルトディレクトリ
```
C:\Users\{User}\AppData\Local\Google\Chrome\User Data\Profile 1
```
## chrome application
chrome.exeのパスを探す
デフォルトディレクトリ
```
C:\Program Files\Google\Chrome\Application\chrome.exe
```

## chrome driverのパスを探す
なければインストール
zipファイルで任意のディレクトリにダウンロードされる

## リモートデバッグモードで起動
```
& "chrome.exe path" --remote-debugging-port=9222 --user-data-dir="chrome profile path"
```
アクセスが許可されたアカウントでログインしておく

## install library
```
pip install selenium
pip install bs4
pip install python-dotenv
```

## env
```.env```ファイルを作成
```
URL = "forms_url"
D_path = "chromedriver.exe path"
port = 9222
```

## run
### 方法１
```
& "chrome.exe path" --remote-debugging-port=9222 --user-data-dir="chrome profile path"
python getpeaple.py > out.txt
```
### 方法２
```
# Chromeをリモートデバッグモードで起動
Start-Process `
    -FilePath "chrome.exe path" `
    -ArgumentList @(
        "--remote-debugging-port=9222", 
        "--user-data-dir=""chrome Profile"""
    )

# 5秒待機して、Chromeが完全に起動するのを待つ
Start-Sleep -Seconds 5

# Pythonスクリプトを実行
& "python.exe path" `
   "getpeaple.py path"
```


