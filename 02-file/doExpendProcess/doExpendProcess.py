'''
提取支出的数字与文字描述
72 米线
110 咖啡
290 烧烤
11 打车
'''
 
import re
 

def main():

    #NUM_REG = r"\d+(\.\d+)?"
    NUM_REG = r"\d+"
    CHN_REG= r"[\u4e00-\u9fa5]+"
   
    ipt = input('提取数字(1)还是文字(2):')

    raw = ""
    lst=[]
    # 读取支出
    with open('02-file/doExpendProcess/expends.txt', 'r', encoding='utf-8') as fp:
        raw = fp.read()

    if ipt == '1':
        lst = re.findall(NUM_REG, raw)
    elif ipt == '2':
        lst = re.findall(CHN_REG, raw)

    for ele in lst:
        print(ele)

if __name__ == "__main__":
    main()