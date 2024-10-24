from dotenv import load_dotenv
import os

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数を取得
URL = os.getenv("URL")
D_path = os.getenv("D_path")
port = os.getenv("port")