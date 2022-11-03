'''
Фигурное катание

Таня любит фигурное катание и хочет узнать результаты своих любимых фигуристов, но не может, так как на сайте с результатами нет функции поиска, и она страдает от этого. Помогите Тане: найдите среди всех таблиц результатов информацию об интересующих её фигуристах.

ФОРМАТ ВВОДА

Строка с первой страницей результатов. На каждой странице результатов есть ровно одна таблица с результатами, состоящая из порядкового номера выступающего, ячейки с именем и ячейками с детализированными результатами. Также на странице находятся ссылка с содержимым "предыдущая таблица результатов" (кроме первой страницы) и ссылка с содержимым "Следующая таблица результатов" (кроме последней страницы).
Строка с фамилией интересующего фигуриста
Строка с перечнем столбцов результатов, информация из которых интересует Таню. Названия столбцов указаны через запятую.
ФОРМАТ ВЫВОДА

Перечень результатов в указанном Таней порядке, результаты из одной таблицы указаны в одной строке через пробел, строки с результатами идут в хронологическом порядке.
Пояснение к примеру 1: результаты фигуриста Плисецкого есть только в двух таблицах, так что выведено две строки в хронологическом порядке (сначала из первой таблицы, потом — из третьей).

Пояснение к примеру 2: результаты фигуриста Кацуки есть только в двух таблицах, так что выведено две строки в хронологическом порядке (сначала из второй таблицы, потом — из третьей).
Пояснение к примеру 3: результаты фигуриста Пролджэ есть только в одной таблице.

Сайт, анализируемый в открытом тесте, можно посмотреть здесь.


При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
import re
from bs4 import BeautifulSoup
# link = 'http://online.hse.ru/python-as-foreign/tasks/fs/example/'
def get_soup(link):
	resp = requests.get(r''+ link)
	resp.encoding = 'utf-8'
	text = resp.text
	soup = BeautifulSoup(text,'lxml')
	return soup
def get_value_from_soup(soup, find_name, args):
	table = soup.find('table')
	if table is None:
		return []
	th = [i.text for i in table.find_all('th')]
	td = [[j.text for j in i.find_all('td')] for i in table.find_all('tr')[1:]]
	headers = {}
	for n, i in enumerate(th):
		headers[i] = n
	out = []
	for i in td:
		if find_name.lower() in i[headers['Имя']].lower():
			for arg in args:
				if arg in headers:
					out.append(i[headers[arg]])
	return out
def find_next_page(soup):
	target = soup.find('a', text='Следующая таблица результатов')
	if target is not None:
		return target.get('href')
	else:
		return False
def process(link,name,args):
	out = []
	soup = get_soup(link)
	values = get_value_from_soup(soup, name, args)
	if values:
		out.append(values)
	next_page = find_next_page(soup)
	if next_page:
		curent_page = ''.join(re.findall(r'(?!.*\/).+',link,0))
		if curent_page:
			new_link = re.sub(curent_page, next_page, link)
			out +=process(new_link,name,args)
		else:
			new_link = link + next_page
			out += process(new_link,name,args)
	return out


link = input()
name = input()
args = input().split(',')
values = process(link, name, args)
for i in values:
	print(' '.join(i))







        
        
        


    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

