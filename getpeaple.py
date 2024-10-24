from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import envar as v
import parsehtml

# Chromeのオプションを設定
chrome_options = Options()
chrome_options.debugger_address = f"localhost:{v.port}"  # デバッグモードで起動したChromeに接続

# ChromeDriverのパスを指定
chrome_driver_path = v.D_path
service = Service(chrome_driver_path)

# 既存のChromeウィンドウに接続
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(v.URL)

parsehtml.parse_html(driver.page_source)

driver.close()