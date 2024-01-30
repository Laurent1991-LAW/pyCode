import urllib.request

url = 'http://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url = url, headers=headers)

# 可从‘快代理’等平台获取
proxies_pool = [{
    'http':'121.230.211.142:325622'
}, {
    'http':'121.230.211.142:325611'
}, ]

# 获取线程池随机元素
import random
proxy = random.choice(proxies_pool)
 
# 1.获取handler对象
handler = urllib.request.ProxyHandler(proxies = proxy)

# 2.获取open对象
opener = urllib.request.build_opener(handler)

# 3.调用open方法
response = opener.open(request)

content = response.read().decode('utf-8')

with open('htmldoc/proxy.html', 'w', encoding='utf-8') as fp:
    fp.write(content)


