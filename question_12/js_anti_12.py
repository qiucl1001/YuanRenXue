# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import base64
import requests
from urllib.parse import urlencode

SUM_TOTAL_LIST = []


def get_one_page(page):
    base_url = 'http://match.yuanrenxue.com/api/match/12?'
    m = base64.b64encode('yuanrenxue{}'.format(page).encode('utf-8')).decode('utf-8')
    params = {
        'page': page,
        'm': m
    }
    dst_url = base_url + urlencode(params)

    with requests.get(
        url=dst_url,
        headers={
            "Host": "match.yuanrenxue.com",
            "Referer": "http://match.yuanrenxue.com/match/12",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.104 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }
    ) as response:
        if response.status_code == 200:
            get_value(response.json())


def get_value(response):
    if 'data' in response.keys() and response.get('data'):
        for item in response.get('data'):
            SUM_TOTAL_LIST.append(item.get('value'))


def main():
    for i in range(1, 6):
        get_one_page(i)
        # break
    total_sums = sum(SUM_TOTAL_LIST)
    print(total_sums)


if __name__ == '__main__':
    main()
