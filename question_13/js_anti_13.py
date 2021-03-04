# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import re
import requests


SUM_TOTAL_LIST = []


def get_cookie(session):
    get_cookie_url = 'http://match.yuanrenxue.com/match/13'
    with session.get(url=get_cookie_url) as response:
        if response.status_code == 200:
            cookie_pattern = re.compile(r"document.cookie=(.*?)';path=/")
            cookie = re.findall(cookie_pattern, response.text)
            if cookie:
                yuanrenxue_cookie = cookie[0].replace("')+('", '').replace("')+", '').replace("('", '')
                return yuanrenxue_cookie


def get_value(session, page):
    dst_url = 'http://match.yuanrenxue.com/api/match/13?page={}'.format(page)
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if all([
                'data' in res.keys(),
                res.get('data')
            ]):
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))
                # print(SUM_TOTAL_LIST)


def main():
    session = requests.Session()
    headers = {
        'Referer': 'http://match.yuanrenxue.com/match/13',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.104 Safari/537.36'
    }
    session.headers = headers
    yuanrenxue_cookie = get_cookie(session)
    new_cookie = {
        yuanrenxue_cookie.split('=')[0]: yuanrenxue_cookie.split('=')[1]
    }
    session.cookies.update(new_cookie)
    for page in range(1, 6):
        get_value(session, page)
        # break
    sum_total = sum(SUM_TOTAL_LIST)
    print(SUM_TOTAL_LIST)
    print(sum_total)


if __name__ == '__main__':
    main()

