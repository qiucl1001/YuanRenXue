# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import execjs
import requests
from urllib.parse import urlencode


SUM_TOTAL_LIST = []

HEADERS = {
        "Host": "match.yuanrenxue.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36",
        "Referer": "http://match.yuanrenxue.com/match/16",
        'X-Requested-With': 'XMLHttpRequest'
    }


def get_m_value():
    with open('js_anti_16.js', 'r', encoding='utf-8') as f:
        js_str = f.read()

    return execjs.compile(js_str).call('get_m_value')


def get_one_page(headers, page):
    base_url = 'http://match.yuanrenxue.com/api/match/16?'
    m_value, timestamp = get_m_value()
    query_string = {
        'page': page,
        'm': m_value,
        't': timestamp
    }
    dst_url = base_url + urlencode(query_string)

    with requests.get(url=dst_url, headers=headers) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                print(f'第{page}页数据为：', res.get('data'))
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def main():
    for page in range(1, 6):
        if page < 4:
            get_one_page(HEADERS, page)
        else:
            headers = HEADERS.update({
                'User-Agent': 'yuanrenxue.project'
            })
            get_one_page(headers, page)

    print(SUM_TOTAL_LIST)
    print(sum(SUM_TOTAL_LIST))


if __name__ == '__main__':
    main()

