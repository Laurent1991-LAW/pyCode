
from openpyxl import Workbook
import json



result = []
sorted_res = []
unsplit_trans = '';
trans_list = [];
template = "S{_season}E{_ep}"



def main():
    with open('res.txt', 'r', encoding='utf-8') as fp:
        sorted_res = json.load(fp)

    with open('beTrans.txt', 'r', encoding='utf-8') as fp:
        unsplit_trans = fp.read()

    trans_list = unsplit_trans.split('\n')

    outwb = Workbook()
    outws = outwb.worksheets[0]
        
    outws.append(['排名','剧集','剧名','评分','英文简介','中文简介'])

    for index in range(0,216):
        ele = []
        ele.append(str(index+1))
        ele.append(template.format(_season = str(sorted_res[index]['season_num']).zfill(2),
                                 _ep = str(sorted_res[index]['episode_num']).zfill(2)))
        ele.append(sorted_res[index]['title'])
        ele.append(sorted_res[index]['rate'])
        ele.append(sorted_res[index]['description_en'].strip())
        ele.append(trans_list[index])
        outws.append(ele)

    
    outwb.save('test.xlsx')
    print('数据存入excel成功')

if __name__ == "__main__":
    main()
