from googletrans import Translator


def translate_text(text):
    translator = Translator(service_urls=['translate.google.com'])
    translation = translator.translate(text, src='zh-CN', dest='en')
    return translation.text


# 读取SQL文件
with open('/Users/luoran/Desktop/dockerfile_sql/script/ry_20231130.sql', 'r', encoding='utf-8') as file:
    sql_content = file.readlines()

# 翻译中文内容并写入新文件
with open('/Users/luoran/Desktop/dockerfile_sql/output.sql', 'w', encoding='utf-8') as file:
    for line in sql_content:
        if "comment" in line:  # 判断是否包含 'comment'
            file.write(line)  # 不翻译包含 'comment' 的行
        else:
            start = line.find("'")  # 查找第一个单引号位置
            end = line.find("'", start + 1)  # 查找第二个单引号位置
            while start != -1 and end != -1:  # 迭代查找并翻译多个单引号中的中文内容
                text_to_translate = line[start+1:end]  # 提取单引号内的中文内容
                if text_to_translate is not None and text_to_translate.strip(): 
                    translated_text = translate_text(text_to_translate)  # 翻译中文内容
                    line = line.replace(text_to_translate,
                                        translated_text)  # 替换原始行中的中文内容
                start = line.find("'", end + 1)  # 继续查找下一个单引号位置
                end = line.find("'", start + 1)  # 继续查找下一个单引号位置
            file.write(line)
