import urllib.request
import json


headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
    'Cookie':'MUID=1EE71B8A43AD6FDA35BF08B042D76EF5; SUID=M; MUIDB=1EE71B8A43AD6FDA35BF08B042D76EF5; _EDGE_S=SID=112699629230692B190F8A2093E968C2; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=816FE2BEA06F4F03B1FDFC938EB05556&dmnchg=1; _SS=SID=112699629230692B190F8A2093E968C2; _tarLang=default=zh-Hans; _TTSS_IN=hist=WyJlbiIsImF1dG8tZGV0ZWN0Il0=; _TTSS_OUT=hist=WyJ6aC1IYW5zIl0=; SRCHHPGUSR=SRCHLANG=zh-Hans&PV=15.0.0; SRCHUSR=DOB=20230702&T=1688270549000',
}

def my_translate(text):

    print("输入的翻译文本为："+text)

    url = 'https://www.bing.com/ttranslatev3?isVertical=1&&IG=64F40B6CDE734C098A57BBA40E7E78EE&IID=translator.5027'

    data = {
        'fromLang':'en',
        'text':text,
        'to':'zh-Hans',
        'token':'t3a99eMrLKADbCzP2X41vM5Ur0NFK8_F',
        'key':'1688270549047',
        'tryFetchingGenderDebiasedTranslations':'true',
    }

    request = urllib.request.Request(url=url,
                                     data=urllib.parse.urlencode(
                                         data).encode('utf-8'),
                                     headers=headers)

    response = urllib.request.urlopen(request)

    result = response.read().decode('utf-8')

    jsonRes = json.loads(result)

    
    return jsonRes[0]['translations'][0]['text']


text = 'On 14 August 2013, UPS Airlines Flight 1354 clips the tops of trees'

print(my_translate(text))