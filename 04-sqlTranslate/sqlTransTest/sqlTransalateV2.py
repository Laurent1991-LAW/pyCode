import re
from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn'])


def translate_sql_file(input_file, output_file):
    translated_sql = ""
    with open(input_file, 'r', encoding='utf-8') as input_file:
        contents = input_file.read()

        pattern = r"insert into.*?values\s*\((.*?)\);"
        matches = re.findall(pattern, contents, re.IGNORECASE | re.DOTALL)

        for match in matches:
            values = match.split(',')
            translated_values = []
            for value in values:
                value = value.strip()
                if value.startswith("'") and value.endswith("'"):
                    chinese_text = re.findall(r"'(.*?)'", value)[0]
                    translated_text = translator.translate(
                        chinese_text, dest='zh-cn').text
                    value = value.replace(chinese_text, translated_text)
                translated_values.append(value)
            translated_sql += f"INSERT INTO {match}({','.join(translated_values)});\n"

    with open(output_file, 'w', encoding='utf-8') as output_file:
        output_file.write(translated_sql)

# 测试
translate_sql_file(
    "/Users/luoran/Desktop/dockerfile_sql/script/ry_20231130.sql", "/Users/luoran/Desktop/dockerfile_sql/output.sql")
