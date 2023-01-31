import ssl
import requests
import openpyxl
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
import os
import time
from datetime import datetime
import json
# from cfg import *
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
pu="\033[1;35m"
ye="\033[1;33m"

CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

wb = openpyxl.Workbook()
wb.active = 0
sheet = wb.active
proxy_key= '82f2bae68f1a03ffba8d809d1abdb396'
os.system('cls')

print(f"""
{re}╔═╗{cy}┌─┐{re}═╦═
{re}╚═╗{cy}├─┤{re} ║
{re}╚═╝{cy}┴ ┴{re}═╩═
by https://github.com/foxius
""")
def main():
    proxies = {
            'http': 'http://UmGEX1:EBeRANduq6am@mproxy.site:11823',
            'https': 'http://UmGEX1:EBeRANduq6am@mproxy.site:11823'
            }
    session = requests.session()
    adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
    session.mount("https://", adapter)
    p=1
    urls_vag= [f'https://www.avito.ru/all/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/volkswagen/novyy-ASgBAgICBEQKJKwJ~GPgtg24mSjQtw3ShTM?cd=1&f=ASgBAgECBEQKJKwJ~GPgtg24mSjQtw3ShTMBRcaaDBd7ImZyb20iOjUwMDAsInRvIjo1NTAwfQ&s=0&p={p}&user=1', f'https://www.avito.ru/all/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/volkswagen/novyy-ASgBAgICBEQKJKwJ~GPgtg24mSjQtw3ShTM?cd=1&f=ASgBAgECBUQKJKwJ~GPgtg24mSjQtw3ShTOK4Q2W21wBRcaaDBd7ImZyb20iOjU1MDEsInRvIjo3MDAwfQ&p={p}&user=1',f'https://www.avito.ru/all/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/volkswagen/novyy-ASgBAgICBEQKJKwJ~GPgtg24mSjQtw3ShTM?cd=1&f=ASgBAgECBUQKJKwJ~GPgtg24mSjQtw3ShTOK4Q2W21wBRcaaDBh7ImZyb20iOjcwMDEsInRvIjoxMDAwMH0&p={p}&user=1',f'https://www.avito.ru/all/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/volkswagen/novyy-ASgBAgICBEQKJKwJ~GPgtg24mSjQtw3ShTM?cd=1&f=ASgBAgECBUQKJKwJ~GPgtg24mSjQtw3ShTOK4Q2W21wBRcaaDBl7ImZyb20iOjEwMDAxLCJ0byI6MTYwMDB9&p={p}&user=1', f'https://www.avito.ru/all/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/volkswagen/novyy-ASgBAgICBEQKJKwJ~GPgtg24mSjQtw3ShTM?cd=1&f=ASgBAgECBUQKJKwJ~GPgtg24mSjQtw3ShTOK4Q2W21wBRcaaDBl7ImZyb20iOjE2MDAxLCJ0byI6NDAwMDB9&p={p}&user=1']
    for url in urls_vag:
        # url = f"https://www.avito.ru/all/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/volkswagen/novyy-ASgBAgICBEQKJKwJ~GPgtg24mSjQtw3ShTM?cd=1&f=ASgBAgECBEQKJKwJ~GPgtg24mSjQtw3ShTMBRcaaDBl7ImZyb20iOjE3MDAxLCJ0byI6NDAwMDB9&user=1"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 OPR/90.0.4480.117'}
        r = session.request('GET',url, headers = headers, proxies=proxies)
        soup = bs(r.content, 'html.parser')
        captcha = soup.find('h1', text='Доступ ограничен: проблема с IP')
        global page
        if captcha:
            change_ip()
        else:
            pages = soup.find_all('span', class_="pagination-item-JJq_j")
            page = int(pages[7].text)
            for p in range(1, page):
                r = session.request('GET', url, headers = headers, proxies=proxies)
                soup = bs(r.content, 'html.parser')
                for div in soup.find_all("div", class_="iva-item-body-KLUuy"):
                    title = div.find_all("h3", class_ = "title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO")
                    manufacturer = div.find_all("span", class_="iva-item-text-Ge6dR iva-item-textColor-gray44-S6NCQ text-text-LurtD text-size-s-BxGpL")
                    number = div.find_all("div", class_ = "iva-item-text-Ge6dR iva-item-noaccent-_yEU8 text-text-LurtD text-size-s-BxGpL")
                    price = div.find_all("span", class_="price-text-_YGDY text-text-LurtD text-size-s-BxGpL")
                    description = div.find_all("div", class_="iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL")
                    link = div.find_all("a", class_ = "link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH")
                    _l = zip(title, manufacturer, number, price, description, link)
                    try:
                        for i in _l:
                            print(f"{gr}Запись: ", i[0].text, i[1].text, i[2].text, i[3].text, sep=' ', end="\n")
                            link = f"https://avito.ru{i[5].get('href')}"
                            sheet.append([i[1].text, i[2].text, i[3].text, i[4].text, link])
                    except:
                        continue
                    wb.save("1.xlsx")    
def change_ip():
    now = datetime.now().strftime("%H:%M:%S")
    print(f"{ye}[{now}] {pu}Меняю IP{cy}")
    proxy = f"https://mobileproxy.space/reload.html?proxy_key={proxy_key}&format=json"
    huy = requests.get(proxy)
    data = json.loads(huy.text)
    if data['status'] == 'OK':
        now = datetime.now().strftime("%H:%M:%S")
        print(f"{ye}[{now}] {gr}Cмена IP-адреса прошла успешно! Новый IP - {cy}{data['new_ip']}")
    if data['status'] == 'ERR':
        now = datetime.now().strftime("%H:%M:%S")
        print(f"{ye}[{now}] {re}Произошла ошибка при смене IP-адреса. Повторная смена{cy}")
        print(f"{ye}[{now}] {pu}Меняю IP{cy}")
        proxy = f"https://mobileproxy.space/reload.html?proxy_key={proxy_key}&format=json"
        huy = requests.get(proxy)
        data = json.loads(huy.text)
        if data['status'] == 'OK':
            now = datetime.now().strftime("%H:%M:%S")
            print(f"{ye}[{now}] {gr}Cмена IP-адреса прошла успешно! Новый IP - {cy}{data['new_ip']}")
        if data['status'] == 'ERR':
            now = datetime.now().strftime("%H:%M:%S")
            print(f"{ye}[{now}] {re}Произошла ошибка при смене IP-адреса. Повторная смена{cy}")
            print(f"{ye}[{now}] {pu}Меняю IP{cy}")
            proxy = f"https://mobileproxy.space/reload.html?proxy_key={proxy_key}&format=json"
            huy = requests.get(proxy)
        time.sleep(1)
    time.sleep(1)

if __name__ == "__main__":
    main()