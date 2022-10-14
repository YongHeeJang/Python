# 웹크롤러를 이용해서 환율 정보 가져오기
from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

print(cc.convert(1, 'USD', 'KRW'))

import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        'User-Agent' : 'Mozilla/5.0', # 웹크롤러가 아니라 브라우저인 것처럼 해주기 위해서 한 것 
        'Content-Type' : 'text/html; charest=utf-8'
    }
    response = requests.get('http://kr.investing.com/curreycies/{}-{}'.format(target1, target2), headers=headers)
    
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})

    print(containers.text)
# beautifulsoup4는 웹크롤링해주는 사이트
# 만약 사이트에서 beautifulsoup를 이용해 웹크롤링하는 것을 막았다면, 셀레늄으로 할 수도 있다.
# 셀레늄은 그 자체가 웹브라우저이기 때문에, 대부분의 웹페이지는 뷰티풀수프와 셀레늄으로 크롤링할 수 있다. 

get_exchange_rate('usd', 'krw')