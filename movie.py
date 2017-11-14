from bs4 import BeautifulSoup
import requests
import json

base_web = 'https://movie.douban.com/'
teleplay_base = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'
movie_base = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&page_limit=50&page_start=0'

f_hm = open('hot_movie.csv','w',encoding='utf_8_sig')
f_tv = open('teleplay.csv','w',encoding='utf_8_sig')
f_mv = open('movie.csv','w',encoding='utf_8_sig')

request_hot = requests.get(base_web)
sp = BeautifulSoup(request_hot.text,'lxml')
hot_movie = sp.select('#screening > div.screening-bd > ul > li')
for i in hot_movie:
    a = i.contents[1].contents[1].contents[1].contents[1].attrs
    b = i.getText().split('\n')[11]
    c = i.contents[1].contents[7].contents[0].contents[0].attrs
    f_hm.write(a['alt']+','+b+','+c['href']+'\n')
    print(a['alt']+'\t评分：'+b+'\t购票网址：'+c['href'])


request_tv = requests.get(teleplay_base)
js_tv = json.loads(request_tv.content)
for each in js_tv['subjects']:
    pass
    f_tv.write(each['title']+','+each['rate']+','+each['url']+'\n')
    print(each['title']+'\t评分：'+each['rate']+'\t豆瓣网址：'+each['url'])


request_tv = requests.get(movie_base)
js_tv = json.loads(request_tv.content)
for each in js_tv['subjects']:
    pass
    f_mv.write(each['title']+','+each['rate']+','+each['url']+'\n')
    print(each['title']+'\t评分：'+each['rate']+'\t豆瓣网址：'+each['url'])

f_hm.close()
f_mv.close()
f_tv.close()