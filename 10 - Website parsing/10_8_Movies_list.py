'''
Список фильмов

Дима хочет ознакомиться с самыми лучшими фильмами в истории и изучает списки с рекомендациями. Напишите программу, которая поможет ему выбрать такие фильмы для просмотра, которые рекомендованы сразу во всех списках. 

ФОРМАТ ВВОДА

Строки со ссылками на страницы со списками фильмов, по одной ссылке в строке.
После всех ссылок идёт строка со словом “конец”.
На каждой странице со списками фильмов указано Название фильма, Режиссёр, Исполнители главных ролей, Рейтинг фильма (целое число от 1 до 5 включительно) и Год выхода на экраны (целое положительное число).
ФОРМАТА ВЫВОДА

Список фильмов по алфавиту (без учёта регистра), по одному названию в строке.
Cтраницы, анализируемые в открытом тесте, можно посмотреть здесь и здесь.


При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup
from functools import reduce

def common_member(a, b):
    a_set = set(a)
    b_set = set(b)
 
    if (a_set & b_set):
        return a_set & b_set
    else:
        return 0

my_list = []
output1 = []
output2 = []
i = 0

while True:
    weblink = input()
    if weblink == "конец":
        break
    else:
        my_list.append([])
        site = requests.get(weblink)
        site.encoding = 'utf-8'
        soup = BeautifulSoup(site.text, 'lxml')
        for link in soup.find_all('td'):
            my_list[i].append(link.get_text())
        i = i + 1

for i in range(0, len(my_list)):
    my_list[i] = my_list[i][0::5]
    
res = list(reduce(lambda i, j: i & j, (set(x) for x in my_list)))

final_output = sorted(res, key = str.lower)

for i in range(0, len(final_output)):
    print(final_output[i])


        
        
        


    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

