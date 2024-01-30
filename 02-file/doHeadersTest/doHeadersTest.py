'''
@File    :   doHeadersTest.py
@Time    :   2023/12/12 11:47:11
@Author  :   LUO Ran
@Version :   1.0
@Desc    :   
    # 基于source中的内容 以及 输入的一级目录数 
    # 生成一级目录, 二级目录标题, 及三层三级目录(暂无标题)
    # 若二级目录有hands on, 则不生成二级, 而是在 三层三级目录后添加hands on的文本
'''

import re

FIRST_LEVEL = "# "
SECOND_LEVEL = "## "
THIRD_LEVEL = "### "
HAND_MARK = 'hands'
HAND_ON_STR = 'Hands On'
PREFIX_TO_REMOVE = 'DVAC02 '

def main():
    firstLevelNum = '24'
    secondLevelNum = 1

    with open('./doHeadersTest/source.txt', 'r', encoding='utf-8') as fp:
            read = fp.read()
    
    list = read.split('\n')

    for each in list:
         
        if (each.endswith('mp4')):
            match = re.search(r' - (.+?)\.', each)
            if match:
                title = match.group(1).removeprefix(PREFIX_TO_REMOVE)

                if HAND_MARK in title.lower():
                    print(HAND_ON_STR)
                else:
                    print(SECOND_LEVEL+firstLevelNum + "." + str(secondLevelNum) + " " +title)
                    print(THIRD_LEVEL+firstLevelNum+ "." + str(secondLevelNum) + ".1")
                    print(THIRD_LEVEL+firstLevelNum+ "." + str(secondLevelNum) + ".2")
                    print(THIRD_LEVEL+firstLevelNum+ "." + str(secondLevelNum) + ".3")
                    secondLevelNum+=1

        else:
             match = re.search(r' - (.+)', each)
             if match:
                title = match.group(1)
                print(FIRST_LEVEL + firstLevelNum + ". " +title)

if __name__ == "__main__":
    main()
