import urllib.parse
import urllib.request
import re
from bs4 import BeautifulSoup

#запрашиваем название,делим его на слова, передаем в форму, получаем страницу с результатами поиска
zapros=input()
zaprosspis=zapros.split()
args={'query':zaprosspis}
ec=urllib.parse.urlencode(args)
f = urllib.request.urlopen("http://zoon.ru/search/" + "?" + ec)
respData = f.read()
rutext = respData.decode("utf-8")
#достаем из html-кода страницы нужные нам ссылки (или ссылку, если ресторан с таким названием один)
soup1=BeautifulSoup(rutext, 'html.parser')#страница результатов,обработанная bs
spisok=[]
for elem in soup1(text=re.compile(zapros)):
	spisok.append(elem.parent)
#получили список ссылок по данному ресторану с его названием, но они в тегах html	
spisstroka=str(spisok)
urls = re.findall(r'href=[\'"]?([^\'" >]+)', spisstroka)
#в итоге получили список url-ов, которые нам нужны
#теперь идем по каждому url на страницу ресторана, берем оттуда отзывы, чистим,пишем в txt-файл
for url in urls:
    url2=urllib.parse.urljoin(url, 'reviews/')    #надо открыть полную страницу со всеми отзывами, а не с двумя первыми
    x=urllib.request.urlopen(url2)
    text=x.read()
    soup = BeautifulSoup(text, 'html.parser')    
    a=soup.find_all('div', {'class': 'simple-text comment-text js-comment-text'})
    ex=list(a)
    outfile = open ('reviews.txt', 'a', encoding='utf-8') #режим дозаписи
    for element in ex:
        stroka=str(element)
        element1=re.sub('<[^>]*>', '', stroka)
        element2=re.sub('\xa0', ' ', element1)
        outfile.write(element2+"\n")
outfile.close()	
#поскольку у меня непрогнозируемо при частых запросах на /reviews уходит в 404,прописать, что в случае, если страница не найдена, брать первые два отзыва с url, а не url2; но,  несмотря на ошибку, файлы обычно в файл пишутся. Кроме того, пока не разбито на условия, что если несколько одинаковых названий, запрашивать улицу и искать по тегу хтмл ресторан именно на этой улице. Пока все одноименные воспринимаются как один объект.Не прописано условие, что делать, если рецензий нет: просто будет пустой файл. Обе страницы проверены на роботпарсер, он разрешает. 
