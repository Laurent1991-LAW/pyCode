import urllib.request
import json
import operator
import re
from bs4 import BeautifulSoup

imdb_base_url = 'https://www.imdb.com/title/tt0386950/episodes?season='

trans_url = 'https://www.bing.com/ttranslatev3?isVertical=1&&IG=64F40B6CDE734C098A57BBA40E7E78EE&IID=translator.5027'

trans_data = {
        'fromLang':'en',
        'to':'zh-Hans',
        'token':'t3a99eMrLKADbCzP2X41vM5Ur0NFK8_F',
        'key':'1688270549047',
        'tryFetchingGenderDebiasedTranslations':'true',
    }

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}


# 翻译简介
def my_translate(text):
    trans_data['text'] = text
    request = urllib.request.Request(url=trans_url,
                                     data=urllib.parse.urlencode(
                                         trans_data).encode('utf-8'),
                                     headers=headers)
    response = urllib.request.urlopen(request)
    result = response.read().decode('utf-8')
    jsonRes = json.loads(result)
    print("请求bing翻译相应："+result)
    return jsonRes[0]['translations'][0]['text']

# 生成本地html文件
def generate_local_html(content, season_num):
    with open('htmldoc/maydayS{_season_num}.html'.format(_season_num = season_num), 'w', encoding='utf-8') as fp:
        content = fp.write(content)

# 解析html文件生成episode对象
def decode_html(content, season_num):
    soup = BeautifulSoup(content, 'lxml')
    for info in soup.find_all(class_='info'):
        desc = info.find(class_='item_description').string
        ele = {
            'season_num': season_num,
            'episode_num':info.meta['content'],
            'title':info.find(attrs={'itemprop': 'name'})['title'],
            'rate':info.find(class_='ipl-rating-star__rating').string,
            'description_en':desc,
            'description_cn':''

        }
        result.append(ele)

# 将排序后的列表输出txt
def generate_txt():
    with open('htmldoc/result.txt', 'w', encoding='utf-8') as fp:
        json.dump(sorted_res, fp)

# 请求imdb获取html文件保存到本地
def fetch_by_seasons(start, end):
    for season_num in range(23,24):
        print("开始获取第{_season_num}季数据".format(_season_num = season_num))
        imdb_url = imdb_base_url + str(season_num)
        request = urllib.request.Request(url = imdb_url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        generate_local_html(content, season_num)
    

# 读取html解析为对象列表保存到本地
def decode_html_local_save():
    for season_num in range(1,24):
        with open('htmldoc/maydayS{_season_num}.html'.format(_season_num = season_num), 'r', encoding='utf-8') as fp:
            content = fp.read()
            decode_html(content, season_num)
        print("第{_season_num}季数据解析获取结束".format(_season_num = season_num))   
        print("所有html文件已解析结束，开始排序...")
        sorted_res = sorted(result, key=operator.itemgetter('rate'), reverse=True)
        print("排序结束，开始写入本地结果文件...")
        with open('res.txt', 'w', encoding='utf-8') as fp:
            json.dump(sorted_res, fp)

# 将排序后结果初始化到内存
def init_sorted_res():
    with open('res.txt', 'r', encoding='utf-8') as fp:
        sorted_res = json.load(fp)
        print("sorted result:" + json.dumps(sorted_res))

# 获取英文介绍
def decode_html_local_save():   
    with open('res.txt', 'r', encoding='utf-8') as fp:
        sorted_res = json.load(fp)
        print("sorted result:" + json.dumps(sorted_res))

    with open('toTrans.txt', 'a', encoding='utf-8') as fp:
        
        for ele in sorted_res:
            
            desc = ele['description_en'].strip()
            fp.write(desc)

result = []
sorted_res = []
unsplit_trans = '';
trans_list = [];
template = "总排名: {_index}/216\n剧集: S{_season}E{_ep}\n剧名: {_title}\n评分: {_rate}\n简介: {_desc}\n\n"


# 主函数
def main():
    with open('res.txt', 'r', encoding='utf-8') as fp:
        sorted_res = json.load(fp)

    with open('beTrans.txt', 'r', encoding='utf-8') as fp:
        unsplit_trans = fp.read()

    trans_list = unsplit_trans.split('\n')

    with open('finalRes.txt', 'a', encoding='utf-8') as fp:
        for index in range(0,216):
            
            desc = sorted_res[index]['description_en'].strip() + " " + trans_list[index]

            fp.write(template.format(_index = str(index+1),
                                     _season = sorted_res[index]['season_num'],
                                     _ep = sorted_res[index]['episode_num'],
                                     _title = sorted_res[index]['title'],
                                     _rate = sorted_res[index]['rate'],
                                     _desc = desc,
                                     ))
        
            

if __name__ == "__main__":
    main()


    










