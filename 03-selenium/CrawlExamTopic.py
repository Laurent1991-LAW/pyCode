'''
爬取examenTopic的SAP全部题目和答案
20230103-遗留问题

1.topic1需去除
解决办法: 由于topic1在div标签内部的span标签内, 因此可以用以下xpath语句去除
'//div[@class="card-header text-white bg-primary"]/text()[not(parent::span)]'

2.图片问题
解决办法: 由于文本与图片是穿插出现, 比如xxx文本:图片:xxx文本, 为确保顺序, 无法使用selenium,
替代办法为使用BeautifulSoup来解析得到的innerHTML以方便提取文本和图片信息，
因为Selenium本身并不直接提供这样的解析功能 ---> CrawlExamTopic2.0

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as webDriverWait
from io import StringIO

base_url='https://www.examtopics.com/exams/amazon/aws-certified-solutions-architect-professional-sap-c02/view/'
index = 1
ENTER_POINT ='\n'

def doProcessExtractResult(question_titles, question_bodys, question_options_lst, answers_lst):
    buffer = StringIO()
    
    for index, title in enumerate(question_titles):
        buffer.write(title.text)
        buffer.write(ENTER_POINT)
        buffer.write(question_bodys[index].text)
        buffer.write(ENTER_POINT)
        buffer.write(question_options_lst[index].text)
        buffer.write(ENTER_POINT)
        buffer.write(answers_lst[index].text)
        buffer.write(ENTER_POINT)
    
    return buffer.getvalue()  # 获取最终的字符串
    
    

def doProcessBoxUnit(txt):
    print(txt)

def crawlPage(url):
    txt = ''
    print(f'开始爬取第[{index}]页考题及答案')
    print(url)
    driver = webdriver.Chrome()
    driver.get(url)

    webDriverWait(driver, 100).until(
        # 此处若元素不出现需手动完成captcha验证 
        ec.presence_of_element_located((By.XPATH, '//span[@class="correct-answer"]'))
    )

    # 需点击reveal solution才能提取到答案
    btns = driver.find_elements(By.XPATH, '//a[@class="btn btn-primary reveal-solution d-print-none"]')
    for btn in btns:
        btn.click()
    
    # 获取标题
    question_titles = driver.find_elements(By.XPATH,'//div[@class="card-header text-white bg-primary"]/text()[not(parent::span)]')
    # 获取题干
    question_bodys = driver.find_elements(By.XPATH, '//div[@class="card exam-question-card"]/div/p[@class="card-text"]')
    # 获取选项
    question_options_lst = driver.find_elements(By.XPATH, '//div[@class="card exam-question-card"]/div/div/ul')
    # 获取正确答案
    answers_lst = driver.find_elements(By.XPATH, '//span[@class="correct-answer"]')

    return doProcessExtractResult(question_titles, question_bodys, question_options_lst, answers_lst)


# 以页为单位写入txt
def doWrite2Txt(txt):
     with open('finalRes.txt', 'a', encoding='utf-8') as fp:
         fp.write(txt)


# 获取当前页面url
def getUrl(index):
    if index > 1:
        return base_url + str(index) + '/'
    else:
        return base_url

def my_function():
    global index
    while (index < 2):
        doWrite2Txt(crawlPage(getUrl(index)))
        index += 1
        

if __name__ == "__main__":
    my_function()