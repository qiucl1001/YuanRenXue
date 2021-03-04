# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
import execjs
import requests

SUM_TOTAL_LIST = []


def get_js_str(session):
    js_url = 'http://match.yuanrenxue.com/api/match/14/m'
    with session.get(url=js_url) as response:
        if response.status_code == 200:
            res = response.text
            with open('js_anti_14.js', 'r', encoding='utf-8') as f:
                m_js = f.read()
                with open('js_anti_new_14.js', 'w', encoding='utf-8') as fp:
                    fp.write('var window=global;\n' + res + '\n' + m_js)


def get_one_page(session, page):
    dst_url = f'http://match.yuanrenxue.com/api/match/14?page={page}'
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                print(f'第{page}页数据为：', res.get('data'))
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def get_m():
    with open('js_anti_new_14.js', 'r', encoding='utf-8') as f:
        js_str = f.read()
    return execjs.compile(js_str).call('get_m_cookie', 2).replace('m=', '').replace(';path=/', '')


def main():
    session = requests.Session()
    headers = {
        "Host": "match.yuanrenxue.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36",
        "Origin": "http://match.yuanrenxue.com",
        "Referer": "http://match.yuanrenxue.com/match/14",
        "X-Requested-With": "XMLHttpRequest"
    }
    session.headers = headers

    for page in range(1, 6):
        get_js_str(session)
        if page < 4:
            session.cookies.update({
                'mz': 'TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xMDQgU2FmYXJpLzUzNy4zNixbb2JqZWN0IE5ldHdvcmtJbmZvcm1hdGlvbl0sdHJ1ZSwsW29iamVjdCBHZW9sb2NhdGlvbl0sOCxlbixlbiwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xMDQgU2FmYXJpLzUzNy4zNixHb29nbGUgSW5jLiwsW29iamVjdCBEZXByZWNhdGVkU3RvcmFnZVF1b3RhXSxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLDgyNCwwLDAsMTUzNiwyNCw4NjQsW29iamVjdCBTY3JlZW5PcmllbnRhdGlvbl0sMjQsMTUzNixbb2JqZWN0IERPTVN0cmluZ0xpc3RdLGZ1bmN0aW9uIGFzc2lnbigpIHsgW25hdGl2ZSBjb2RlXSB9LCxtYXRjaC55dWFucmVueHVlLmNvbSxtYXRjaC55dWFucmVueHVlLmNvbSxodHRwOi8vbWF0Y2gueXVhbnJlbnh1ZS5jb20vbWF0Y2gvMTQsaHR0cDovL21hdGNoLnl1YW5yZW54dWUuY29tLC9tYXRjaC8xNCwsaHR0cDosZnVuY3Rpb24gcmVsb2FkKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gcmVwbGFjZSgpIHsgW25hdGl2ZSBjb2RlXSB9LCxmdW5jdGlvbiB0b1N0cmluZygpIHsgW25hdGl2ZSBjb2RlXSB9LGZ1bmN0aW9uIHZhbHVlT2YoKSB7IFtuYXRpdmUgY29kZV0gfQ==',
                'm': get_m()
            })
            get_one_page(session, page)
        else:
            session.headers.update({
                'User-Agent': 'yuanrenxue.project'
            })
            session.cookies.update({
                'mz': 'TW96aWxsYSxOZXRzY2FwZSw1LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xMDQgU2FmYXJpLzUzNy4zNixbb2JqZWN0IE5ldHdvcmtJbmZvcm1hdGlvbl0sdHJ1ZSwsW29iamVjdCBHZW9sb2NhdGlvbl0sOCxlbixlbiwwLFtvYmplY3QgTWVkaWFDYXBhYmlsaXRpZXNdLFtvYmplY3QgTWVkaWFTZXNzaW9uXSxbb2JqZWN0IE1pbWVUeXBlQXJyYXldLHRydWUsW29iamVjdCBQZXJtaXNzaW9uc10sV2luMzIsW29iamVjdCBQbHVnaW5BcnJheV0sR2Vja28sMjAwMzAxMDcsW29iamVjdCBVc2VyQWN0aXZhdGlvbl0sTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg4LjAuNDMyNC4xMDQgU2FmYXJpLzUzNy4zNixHb29nbGUgSW5jLiwsW29iamVjdCBEZXByZWNhdGVkU3RvcmFnZVF1b3RhXSxbb2JqZWN0IERlcHJlY2F0ZWRTdG9yYWdlUXVvdGFdLDgyNCwwLDAsMTUzNiwyNCw4NjQsW29iamVjdCBTY3JlZW5PcmllbnRhdGlvbl0sMjQsMTUzNixbb2JqZWN0IERPTVN0cmluZ0xpc3RdLGZ1bmN0aW9uIGFzc2lnbigpIHsgW25hdGl2ZSBjb2RlXSB9LCxtYXRjaC55dWFucmVueHVlLmNvbSxtYXRjaC55dWFucmVueHVlLmNvbSxodHRwOi8vbWF0Y2gueXVhbnJlbnh1ZS5jb20vbWF0Y2gvMTQsaHR0cDovL21hdGNoLnl1YW5yZW54dWUuY29tLC9tYXRjaC8xNCwsaHR0cDosZnVuY3Rpb24gcmVsb2FkKCkgeyBbbmF0aXZlIGNvZGVdIH0sZnVuY3Rpb24gcmVwbGFjZSgpIHsgW25hdGl2ZSBjb2RlXSB9LCxmdW5jdGlvbiB0b1N0cmluZygpIHsgW25hdGl2ZSBjb2RlXSB9LGZ1bmN0aW9uIHZhbHVlT2YoKSB7IFtuYXRpdmUgY29kZV0gfQ==',
                'm': get_m()
            })
            get_one_page(session, page)

    print(SUM_TOTAL_LIST)
    print(sum(SUM_TOTAL_LIST))


if __name__ == '__main__':
    main()



