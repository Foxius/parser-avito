import ssl
import requests
import openpyxl
from bs4 import BeautifulSoup as bs
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager
from requests.packages.urllib3.util import ssl_
import pandas as pd
from pandas import DataFrame
import os


CIPHERS = """ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-SHA256:AES256-SHA"""
class TlsAdapter(HTTPAdapter):

    def __init__(self, ssl_options=0, **kwargs):
        self.ssl_options = ssl_options
        super(TlsAdapter, self).__init__(**kwargs)

    def init_poolmanager(self, *pool_args, **pool_kwargs):
        ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
        self.poolmanager = PoolManager(*pool_args, ssl_context=ctx, **pool_kwargs)

session = requests.session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1)
session.mount("https://", adapter)

wb = openpyxl.open("7.xlsx")
wb.active = 0
sheet = wb.active
for_table = []
https_proxy = "http://203.30.191.56:80"
proxies = {"http": https_proxy}
########################
for p in range(91, 101):#
########################
    url = f"https://www.avito.ru/rossiya/zapchasti_i_aksessuary/zapchasti/dlya_avtomobiley/mercedes_benz-ASgBAgICA0QKJKwJ~GPGxw2soEw?cd=1&f=ASgBAgECBEQKJKwJ~GPQtw3ShTPGxw2soEwBRcaaDBh7ImZyb20iOjUwMDAsInRvIjo0MDAwMH0&p={p}&user=1"
    r = session.request('GET', url)
    soup = bs(r.content, 'html.parser')
    for div in soup.find_all("div", class_="iva-item-body-KLUuy"):
        title = div.find_all("h3", class_ = "title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO")
        manufacturer = div.find_all("span", class_="iva-item-text-Ge6dR iva-item-textColor-gray44-S6NCQ text-text-LurtD text-size-s-BxGpL")
        number = div.find_all("div", class_ = "iva-item-text-Ge6dR iva-item-noaccent-_yEU8 text-text-LurtD text-size-s-BxGpL")
        price = div.find_all("span", class_="price-text-_YGDY text-text-LurtD text-size-s-BxGpL")
        description = div.find_all("div", class_="iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL")
        link = div.find_all("a", class_ = "link-link-MbQDP link-design-default-_nSbv title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH")
        _l = zip(title, manufacturer, number, price, description, link)
        for i in _l:
            print("Страница: ", p, sep="")
            print("Запись: ", i[0].text, i[1].text, i[2].text, i[3].text, sep='|||', end="\n")
            link = f"https://avito.ru{i[5].get('href')}"
            for_table.append([i[1].text, i[2].text, i[3].text, i[4].text, link])
export_csv = DataFrame(for_table).to_excel(r'7.xlsx', index=None, header=None)

