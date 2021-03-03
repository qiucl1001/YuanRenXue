# coding: utf-8
# author: QCL
# software: PyCharm Professional Edition 2018.2.8
"""
   <script>
            window.url = '/api/match/7';
            request = function() {
                var list = {
                    "page": window.page,
                };
                $.ajax({
                    url: window.url,
                    dataType: "json",
                    async: false,
                    data: list,
                    type: "GET",
                    beforeSend: function(request) {},
                    success: function(data) {
                        if (window.page) {} else {
                            window.page = 1
                        }
                        ttf = data.woff;
                        $('.font').text('').append('<style type="text/css">@font-face { font-family:"fonteditor";src: url(data:font/truetype;charset=utf-8;base64,' + ttf + '); }</style>');
                        data = data.data;
                        let html = '';
                        let mad = `<tr><td><span class="ranking-li-span-1"></span></td><td><!--<img class="ranking-li-img-1"src="//ossweb-img.qq.com/images/lol/img/profileicon2/profileicon3018.jpg"alt="玩家头像">--><span class="ranking-li-span-3">九不想乖</span></td><td><span class="ranking-li-span-4"><img src="//ossweb-img.qq.com/images/lol/space/rank/2019pre/season_2019_challenger.png"alt="段位">最强王者Ⅰ</span></td><td><span class="ranking-li-span-5 fonteditor">random_rank_number</span></td><td><span class="ranking-li-span-6">random_level</span></td><td><span class="ranking-li-span-7"><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a><a target="_blank"><img class="ranking-li-img-1"src="/static/match/match7/img/img_number.png"></a></span></td><td><div class="m-ranking-winrate-2"><!--i的width属性等于胜率--><i class="u-ranking-winrate-i"id="ranking_4"data-win="win_rank"style="width: win_rank;"></i><a class="u-winrate ">win_rank</a><a class="u-playnumber">win_number</a></div></td></tr>`;
                        let yyq = 1;
                        let img_num = 1;
                        let imgnum_arr = [1, 8, 3, 2, 4, 5, 7, 5, 15, 3, 9, 8, 5, 1, 3];
                        let level_arr = [1, 4, 3, 2, 9, 15];
                        let name = ['极镀ギ紬荕', '爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风', '影之哀伤', '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王', '噬血啸月', '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅', '逆風祈雨', '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打', '狂卩龙灬巅丷峰', '羁旅天涯.', '南宫沐风', '风恋绝尘', '剑下孤魂', '一蓑烟雨', '领域★倾战', '威龙丶断魂神狙', '辉煌战绩', '屎来运赚', '伱、Bu够档次', '九音引魂箫', '骨子里的傲气', '霸海断长空', '没枪也很狂', '死魂★之灵'];
                        $.each(data, function(index, val) {
                            let ppo = mad;
                            for (let imgnum = 1; imgnum <= 5; imgnum++) {
                                ppo = ppo.replace('img_number', yyq * window.page + imgnum_arr[imgnum])
                            }
                            html += ppo.replace('九不想乖', name[yyq + (window.page - 1) * 10]).replace('win_number', imgnum_arr[yyq] * level_arr[window.page] * 88 + '场').replace(/win_rank/g, imgnum_arr[yyq] + 60 + level_arr[window.page] + '%').replace('random_level', imgnum_arr[yyq] * level_arr[window.page] + 100 * level_arr[window.page]).replace('img_number', yyq * window.page).replace('random_rank_number', val.value.replace(/ /g, '') + 'LP');
                            yyq += 1;
                            img_num += 1
                        });
                        $('.append_result').text('').append(html)
                    },
                    complete: function() {},
                    error: function() {
                        alert('因未知原因，数据拉取失败。可能是触发了风控系统');
                        alert('生而为虫，我很抱歉');
                        $('.page-message').eq(0).addClass('active');
                        $('.page-message').removeClass('active')
                    }
                })
            }
            ;
            request()
        </script>
"""
import re
import base64
import requests
from fontTools.ttLib import TTFont
from xml.dom.minidom import parse

SUCCESS_DATA_LIST = []
BASE_BIN_MAP = {
    '1111111': '7',
    '1111111111': '4',
    '1110101001': '5',
    '1001101111': '1',
    '1001101010': '2',
    '1001010100': '9',
    '1010110010': '3',
    '1010010010': '0',
    '1010101010': '6',
    '1010101011': '8'
}


def get_base_bin_map(page):
    font = parse(f'{page}.xml')  # 读取xml文件
    xml_list = font.documentElement  # 获取xml文档对象，就是拿到DOM树的根
    # getElementsByTagName()
    # 获取xml文档中的某个父节点下具有相同节点名的节点对象的集合,返回的是list
    all_ttg = xml_list.getElementsByTagName('TTGlyph')[1:]
    cipher_dict = {}
    for TTGlyph in all_ttg:
        name = TTGlyph.getAttribute('name')[4:]  # 获取节点的属性值
        # cardinal_num = name.split('_')[1]
        pt = TTGlyph.getElementsByTagName('pt')
        num = ''
        if len(pt) < 10:
            for i in range(len(pt)):
                num += pt[i].getAttribute('on')
        else:
            for i in range(10):
                num += pt[i].getAttribute('on')

        cipher_dict[name] = BASE_BIN_MAP[num]
    return cipher_dict  # {'279': 6, '416': 2, '469': 8, '871': 3, '258': 9, '347': 0, ...}


def get_success_data(page, data):
    cipher_dict = get_base_bin_map(page)
    # data--->[{'value': '&#xf327 &#xc763 &#xb839 &#xf327 '}, {'value': '&#xb834 &#xb293 &#xf327 &#xe952 '},...]
    for item in data:
        res = re.findall(r'\d', item.get('value'))
        num = ''
        for i in range(0, len(res), 3):
            num += cipher_dict.get(''.join(res[i:i + 3]))
        SUCCESS_DATA_LIST.append(int(num))


def get_woff_data(session, page):
    dst_url = f'http://match.yuanrenxue.com/api/match/7?page={page}'
    with session.get(url=dst_url) as response:
        if response.status_code == 200:
            res = response.json()
            if 'woff' in res.keys() and res.get('woff'):
                woff = res.get('woff')
                woff_stream = base64.b64decode(woff)
                # 将woff文件写入本地
                with open('{}.woff'.format(page), 'wb') as f:
                    f.write(woff_stream)
                # 将woff文件转化为对应的xml文件
                woff_2_xml(page)
            success_origin_data = res.get('data') if 'data' in res.keys() and res.get('data') else ''
            # 获取胜点数据
            get_success_data(page, success_origin_data)


def woff_2_xml(page):
    ttf = TTFont('{}.woff'.format(page))
    ttf.saveXML('{}.xml'.format(page))


def main():
    session = requests.Session()
    session.headers = {
        'Host': 'match.yuanrenxue.com',
        'Referer': 'http://match.yuanrenxue.com/match/7',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/88.0.4324.104 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    for page in range(1, 6):
        if page < 4:
            get_woff_data(session, page)
        else:
            session.headers.update({
                'User-Agent': 'yuanrenxue.project'
            })
            get_woff_data(session, page)
        # break

    print(SUCCESS_DATA_LIST)

    names = ['爷灬霸气傀儡', '梦战苍穹', '傲世哥', 'мaη肆風聲', '一刀メ隔世', '横刀メ绝杀', 'Q不死你R死你', '魔帝殤邪', '封刀不再战', '倾城孤狼', '戎马江湖', '狂得像风',
             '影之哀伤',
             '謸氕づ独尊', '傲视狂杀', '追风之梦', '枭雄在世', '傲视之巅', '黑夜刺客', '占你心为王', '爷来取你狗命', '御风踏血', '凫矢暮城', '孤影メ残刀', '野区霸王',
             '噬血啸月',
             '风逝无迹', '帅的睡不着', '血色杀戮者', '冷视天下', '帅出新高度', '風狆瑬蒗', '灵魂禁锢', 'ヤ地狱篮枫ゞ', '溅血メ破天', '剑尊メ杀戮', '塞外う飛龍', '哥‘K纯帅',
             '逆風祈雨',
             '恣意踏江山', '望断、天涯路', '地獄惡灵', '疯狂メ孽杀', '寂月灭影', '骚年霸称帝王', '狂杀メ无赦', '死灵的哀伤', '撩妹界扛把子', '霸刀☆藐视天下', '潇洒又能打']
    res = sorted(zip(SUCCESS_DATA_LIST, names), key=lambda x: x[0], reverse=True)
    print(res)
    success_data, name = res[0]
    print(name)


if __name__ == '__main__':
    main()
    # get_base_bin_map()
