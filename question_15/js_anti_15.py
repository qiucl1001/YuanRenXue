# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
"""
<script>
    fetch('/static/match/match15/main.wasm').then(response =>
        response.arrayBuffer()
    ).then(bytes => WebAssembly.instantiate(bytes)).then(results => {
        instance = results.instance;
        window.q = instance.exports.encode;
        window.m = function (){
            t1 = parseInt(Date.parse(new Date())/1000/2);
            t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
            return window.q(t1, t2).toString() + '|' + t1 + '|' + t2;
        };
        window.url = '/api/match/15';
        request = function(){
            //    点击换页后的操作，先得到翻到了几页
            var list = {
                "m": window.m(),
                "page": window.page,
            };
            $.ajax({
                url: window.url,
                dataType: "json",
                async: false,
                data: list,
                type: "GET",
                beforeSend: function(request) {
                },
                success: function(data) {

                    data = data.data;
                    let html = '';
                    $.each(data, function(index, val) {
                        html += '<td>'+ val.value + '</td>'
                    });
                    $('.number').text('').append(html);
                },
                complete: function() {
                },
                error: function() {
                    alert('因未知原因，数据拉取失败。可能是触发了风控系统');
                    alert('生而为虫，我很抱歉');
                    $('.page-message').eq(0).addClass('active');
                    $('.page-message').removeClass('active');
                }
            });
        };
        request()
    }).catch(console.error);

</script>
"""
import math
import time
import random
import pywasm
import requests
from urllib.parse import urlencode

SUM_TOTAL_LIST = []


def get_one_page(page):
    # t1 = parseInt(Date.parse(new Date())/1000/2);
    t1 = int(time.time())//2

    #  t2 = parseInt(Date.parse(new Date())/1000/2 - Math.floor(Math.random() * (50) + 1));
    t2 = int(time.time())//2 - math.floor(random.random()*50+1)

    # 1. 加载wasm文件
    runtime = pywasm.load('./main.wasm')

    # 2. 调用执行wasm文件中的方法
    r = runtime.exec('encode', [t1, t2])
    m = str(r) + '|' + str(t1) + '|' + str(t2)
    params = {
        'page': page,
        'm': m
    }
    base_url = 'http://match.yuanrenxue.com/api/match/15?' + urlencode(params)
    with requests.get(
        url=base_url,
        headers={
            'Referer': 'http://match.yuanrenxue.com/match/15',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/88.0.4324.104 Safari/537.36'
        }
    ) as response:
        if response.status_code == 200:
            res = response.json()
            if 'data' in res.keys() and res.get('data'):
                for item in res.get('data'):
                    SUM_TOTAL_LIST.append(item.get('value'))


def main():
    for page in range(1, 6):
        get_one_page(page)
        # break
    sum_total = sum(SUM_TOTAL_LIST)
    print(SUM_TOTAL_LIST)
    print(sum_total)


if __name__ == '__main__':
    main()


