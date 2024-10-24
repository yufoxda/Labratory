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
```
python getpeaple.py > out.txt
```