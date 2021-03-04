# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import re
import execjs
import requests


SUM_TOTAL_LIST = []
FLAG = True


def get_ts(session):
    with session.get(url='http://match.yuanrenxue.com/match/9') as response:
        if response.status_code == 200:
            res = response.text
            ts_list = re.findall(r"decrypt.*?(\d+).*?;", res)
            if ts_list:
                ts = ts_list[0]
                return ts


def get_m(ts):
    with open('js_anti_9.js', 'r', encoding='utf-8') as f:
        js_str = f.read()
    return execjs.compile(js_str).call('get_m_value', ts)


def get_one_page(session, page):
    global FLAG
    dst_url = f'http://match.yuanrenxue.com/api/match/9?page={page}'

    if FLAG:
        ts = get_ts(session)
        new_cookie = {
            'm': get_m(ts)
        }
        session.cookies.update(new_cookie)
        FLAG = False

    with session.get(url=dst_url) as response:
        print(response)
        if response.status_code == 200:
            res = response.json()
            print(res)
            if 'data' in res.keys() and res.get('data'):
                print(f'第{page}页数据为：', res.get('data'))
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def main():
    session = requests.Session()
    headers = {
        "Host": "match.yuanrenxue.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36",
        "Referer": "http://match.yuanrenxue.com/match/9",
        "X-Requested-With": "XMLHttpRequest"
    }
    session.headers = headers
    for page in range(1, 6):
        if page < 4:
            get_one_page(session, page)
        else:
            session.headers.update({
                'User-Agent': 'yuanrenxue.project'
            })
            get_one_page(session, page)
        # break
    print(SUM_TOTAL_LIST)
    print(sum(SUM_TOTAL_LIST))


if __name__ == '__main__':
    main()

