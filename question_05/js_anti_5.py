# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import time
import base64
import execjs
import requests

SUM_TOTAL_LIST = []


def get_m_cookie():
    ori_m = str(int(time.time() * 1000))
    ori_f = str(int(time.time())*1000)
    with open('js_anti_md5_5.js', 'r', encoding='utf-8') as f:
        js_str = f.read()
    return [execjs.compile(js_str).call('b', ori_m), ori_m, ori_f]


def get_message_data():
    data = ['432be460375208f0c9138bc45f10bde6',
            'fe985212cc0c4ba76e752f6b057540d5',
            '253e26182f06151f325b941e93fdfa45',
            'ee8de783a8b7afcee5067ec224b1262d,']
    return data


def get_rm4_cookie(str0, str1):
    with open('js_anti_crypto_5.js', 'r', encoding='utf-8') as f:
        js_str = f.read()

    return execjs.compile(js_str).call('get_cookie', str0, str1)


def get_one_page(session, page, ori_m, ori_f):
    dst_url = f'http://match.yuanrenxue.com/api/match/5?page={page}&m={ori_m}&f={ori_f}'
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                print(f'第{page}页数据为：', res.get('data'))
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def bubble_sort():
    n = len(SUM_TOTAL_LIST)
    for j in range(n-1):
        cnt = 0
        for i in range(0, n-1-j):
            if SUM_TOTAL_LIST[i] > SUM_TOTAL_LIST[i+1]:
                SUM_TOTAL_LIST[i], SUM_TOTAL_LIST[i+1] = SUM_TOTAL_LIST[i+1], SUM_TOTAL_LIST[i]
                cnt += 1
        if 0 == cnt:
            return


def main():
    session = requests.Session()
    headers = {
        "Host": "match.yuanrenxue.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36",
        "Origin": "http://match.yuanrenxue.com",
        "Referer": "http://match.yuanrenxue.com/match/5",
        "X-Requested-With": "XMLHttpRequest"
    }
    session.headers = headers

    for page in range(1, 6):
        enc_m, ori_m, ori_f = get_m_cookie()
        str0 = base64.b64encode(ori_m.encode('utf-8')).decode('utf-8')[0:16]
        str1 = ','.join(get_message_data()) + enc_m
        rm4_cookie = get_rm4_cookie(str0, str1)
        if page < 4:
            session.cookies.update({
                "m": enc_m,
                "RM4hZBv0dDon443M": rm4_cookie
            })
            get_one_page(session, page, ori_m, ori_f)
        else:
            session.headers.update({
                'User-Agent': 'yuanrenxue.project'
            })
            session.cookies.update({
                "m": enc_m,
                "RM4hZBv0dDon443M": rm4_cookie
            })
            get_one_page(session, page, ori_m, ori_f)

    print(SUM_TOTAL_LIST)
    print('++++++'*50)
    bubble_sort()
    print(SUM_TOTAL_LIST)
    print(sum(SUM_TOTAL_LIST[-5:]))


if __name__ == '__main__':
    main()


"""
432be460375208f0c9138bc45f10bde6
fe985212cc0c4ba76e752f6b057540d5
253e26182f06151f325b941e93fdfa45
ee8de783a8b7afcee5067ec224b1262d

_$Jy -405537848 _$tT -660478335 _$6_ -389564586
"""
