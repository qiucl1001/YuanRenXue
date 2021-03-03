# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import execjs
import requests

SUM_TOTAL_LIST = []


def get_one_page(session, page):
    dst_url = f'http://match.yuanrenxue.com/api/match/2?page={page}'
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def get_dynamic_cookie():
    with open('js_anti_2.js', 'r', encoding='utf-8') as f:
        js_str = f.read()

    return execjs.compile(js_str).call('get_m_cookie')


def main():
    session = requests.Session()
    headers = {
        "Host": "match.yuanrenxue.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://match.yuanrenxue.com/match/2"
    }
    session.headers = headers
    for page in range(1, 6):
        if page < 4:
            session.headers.update({
                'Cookie': get_dynamic_cookie()
            })
            get_one_page(session, page)
        else:
            session.headers.update({
                'User-Agent': 'yuanrenxue.project',
                'Cookie': get_dynamic_cookie()
            })
            get_one_page(session, page)
        # break
    print(SUM_TOTAL_LIST, len(SUM_TOTAL_LIST))
    print(sum(SUM_TOTAL_LIST))


if __name__ == '__main__':
    main()

