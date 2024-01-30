import pandas as pd
import re


def test1():
    name = "9 - Tour of the AWS Console Services in AWS Simplified Chinese.vtt.vtt.vtt.vtt";
    res = name.replace(".vtt", "");
    print(res);

def test2():
    input_string = "130 - Exponential Backoff Service Limit Increase"

    # 使用正则表达式匹配字符串中的内容
    # match = re.search(r' - (.+?)\.', input_string)
    match = re.search(r' - (.+)', input_string)

    if match:
        # 提取出所需的部分并打印
        result = match.group(1)
        print(result)
    else:
        print("No match found.")


if __name__ == "__main__":
    test2()