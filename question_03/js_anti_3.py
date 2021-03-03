# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import requests

SUM_TOTAL_LIST = []


def get_one_page(session, page):
    dst_url = f'http://match.yuanrenxue.com/api/match/3?page={page}'
    logo_url = 'http://match.yuanrenxue.com/logo'

    session.post(url=logo_url)
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def most_common():
    d = {}
    for i in SUM_TOTAL_LIST:
        d[i] = d.get(i, 0) + 1
    ret = []
    n = None
    for j in sorted(d.items(), reverse=True, key=lambda x: x[1]):
        if len(ret) == 0:
            ret.append(j[0])
            n = j[1]
        else:
            if j[1] == n:
                ret.append(j[0])
            else:
                break
    return ret


def main():
    session = requests.Session()
    headers = {
        "Host": "match.yuanrenxue.com",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36",
        "Accept": "*/*",
        "Origin": "http://match.yuanrenxue.com",
        "Referer": "http://match.yuanrenxue.com/match/3",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en",
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
    # print(max(SUM_TOTAL_LIST, key=SUM_TOTAL_LIST.count))  # 该方法缺陷：当出现同频率的元素只能返回其中的一个
    ret = most_common()
    print(ret)


if __name__ == '__main__':
    main()
