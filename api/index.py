from http.server import BaseHTTPRequestHandler
import re
import requests
from bs4 import BeautifulSoup

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    print("request from", self.client_address)

    # 研究室仮配属 第1回志望調査のURL
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSfVbUU-R2Jfizl_qK5pokotGJ9YyRQ2g_a79tkDDvgtAJGjfA/viewanalytics?pli=1&pli=1&pli=1'
    # 解析済みのhtmlデータ
    r = requests.get(url)
    html = r.text.encode(r.encoding)
    s = BeautifulSoup(html, 'html.parser')
    result = s.find_all('td')

    # 格納
    response=""
    for num in len(result):
        response += (
            f"{result[num]}\n"
        )

    self.send_response(200)
    self.send_header('Content-type','text/plain')
    self.end_headers()
    self.wfile.write(response.encode('utf-8'))
    return