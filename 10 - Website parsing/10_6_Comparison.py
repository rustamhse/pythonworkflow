'''
Сравнение цен в нескольких магазинах

Паша очень хочет купить себе игровую приставку нового поколения, но не хочет переплачивать. Помогите ему найти магазин с самой низкой ценой.

ФОРМАТ ВВОДА

Строка с адресом страницы, где находятся ссылки на страницы магазинов.
Гарантируется, что на странице каждого магазина цена только одна и находится внутри тега <i></i>.
Гарантируется, что все цены уникальны.
ФОРМАТ ВЫВОДА

Строка вида “ссылка: цена руб.” для страницы с самой низкой ценой.
Страницу, анализируемую в открытом тесте, можно посмотреть здесь.

При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup

min_ = 999999999999
my_list = []
weblink = input()
site = requests.get(weblink)
site.encoding = 'utf-8'
soup = BeautifulSoup(site.text, 'lxml')

for link in soup.find_all('a'):
    if link.get('href').endswith('html'):
        current_url = weblink + link.get('href')
        site2 = requests.get(current_url)
        site2.encoding = 'utf-8'
        soup2 = BeautifulSoup(site2.text, 'lxml')
        for link2 in soup2.find_all('i'):
            if int(link2.get_text()) < min_:
                answer_link = current_url
                min_ = int(link2.get_text())
            
print(answer_link + ': ' + str(min_) + ' руб.')
        
        
        


    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

