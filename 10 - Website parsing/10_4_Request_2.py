'''
Максимальная зарплата

Вася хочет найти себе работу и просматривает сайт с вакансиями. Помогите ему найти вакансию с самой большой зарплатой на странице.

ФОРМАТ ВВОДА

Строка с адресом страницы с вакансиями. Все названия вакансий и все зарплаты в таблице уникальны, зарплаты могут быть только целыми числами. 
ФОРМАТ ВЫВОДА

Строка вида “<вакансия>: <зарплата> руб.”
Страницу, анализируемую в открытом тесте, можно посмотреть здесь.

При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'. Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup

def maybeMakeNumber(s):
    if not s:
        return s
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
        return 0

my_list = []
weblink = input()
site = requests.get(weblink)
site.encoding = 'utf-8'
soup = BeautifulSoup(site.text, 'lxml')
for link in soup.find_all('td'):
    my_list.append(link.get_text())

converted = list(map(maybeMakeNumber, my_list))

for i in range (2, len(my_list)):
    if my_list[i] == str(max(converted)):
        print(my_list[i-1] + ': ' + my_list[i] + ' руб.')
    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

