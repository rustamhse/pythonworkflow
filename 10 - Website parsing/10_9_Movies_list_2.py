'''
Фильмография
Дима записался в университете на курс по истории кино, где к каждой паре ему задают посмотреть фильмы определенного режиссера. Напишите программу, которая выберет для Димы фильмы нужного режиссёра. Фильмы должны быть отсортированы по рейтингу (сначала фильмы с оценкой 5, потом с оценкой 4, потом 3, 2 и 1), а фильмы с одинаковым рейтингом (например, Седьмая печать и Земляничная поляна имеют одинаковый рейтинг "5") — по алфавиту.

ФОРМАТ ВВОДА

Строки со ссылками на страницы со списками фильмов, по одной ссылке в строке.
Все строки со ссылками начинаются с http://
После всех ссылок идёт строка с именем режиссёра, рейтинг фильмов которого нужно составить, этой строкой ввод заканчивается.
На каждой странице со списками фильмов именно в этом порядке указаны: Название фильма, Режиссёр, Исполнители главных ролей, Рейтинг фильма (целое число от 1 до 5 включительно) и Год выхода на экраны (целое положительное число). Гарантируется, что на всех страницах рейтинг каждого фильма один и тот же.
ФОРМАТ ВЫВОДА

Список фильмов по рейтингу, в случае одинакового рейтинга -- по алфавиту (без учёта регистра), по одному названию в строке и, в скобках, год выхода фильма на экраны.
Страницы, анализируемые в открытом тесте, можно посмотреть здесь и здесь.


При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup

my_list = []
list_movies = []
list_producers = []
list_dates = []
list_rates = []
indexes_movies = []
indexes_dates = []
indexes_rates = []
d = {}

while True:
    weblink = input()
    if weblink[4] != ":":
        request = weblink
        break
    else:
        site = requests.get(weblink)
        site.encoding = 'utf-8'
        soup = BeautifulSoup(site.text, 'lxml')
        for link in soup.find_all('td'):
            my_list.append(link.get_text())

list_movies = my_list[0::5]
list_producers = my_list[1::5]
list_rates = my_list[3::5]
list_dates = my_list[4::5]

for i in range(0, len(list_producers)):
    if list_producers[i] == request:
        indexes_movies.append(list_movies[i])
        indexes_dates.append(list_dates[i])
        indexes_rates.append(list_rates[i])

        
for i in range(0, len(indexes_movies)):
    key = indexes_movies[i]
    value = indexes_dates[i] + ' ' + indexes_rates[i] 
    d.update({key : value})

d = {key: value for key, value in sorted(d.items())}
d = sorted(d.items(), key=lambda x: x[1].split(' ')[1], reverse=True)

for i in range (0, len(d)):
    print(d[i][0] + ' (' + d[i][1].split(' ')[0] + ')')






        
        
        


    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

