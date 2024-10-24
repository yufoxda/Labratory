from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    ellecters = soup.find_all("div" ,class_="PlcjTc")
    circlegraf = soup.find_all("div",class_="rPU8He")

    print(ellecters)
