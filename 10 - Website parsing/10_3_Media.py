'''
Сохранённые картинки

Вы любите коллекционировать смешные картинки, но вот беда — альбом для сохранённых картинок переполнился. Вы решили написать программу, которая найдёт все адреса картинок (из атрибута src тега img) на странице, чтобы их потом скачать. Если на странице нет ни одной картинки — нужно вывести на экран фразу "NO PICS FOUND".

ФОРМАТ ВВОДА

Строка с адресом страницы с картинками
ФОРМАТ ВЫВОДА

Строки с названиями файлов картинок, по одному названию в строке, в порядке появления адресов в html-коде страницы
или

Строка NO PICS FOUND
Страницы, анализируемые в открытом тесте, можно посмотреть здесь и здесь

При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'. Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup

weblink = input()
site = requests.get(weblink)
site.encoding = 'utf-8'
soup = BeautifulSoup(site.text, 'lxml')
if len(soup.find_all('img')) != 0:
    for link in soup.find_all('img'):
        print(link.get('src'), link.text)
else:
    print('NO PICS FOUND')
    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

