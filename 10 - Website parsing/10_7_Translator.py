'''
Переводчик
Витя приехал в туристическую поездку без гида. К счастью, у него есть сайт с со словарем, где есть таблица перевода слов для двух языков. Помогите ему понять надписи, которые он видит на улицах.

ФОРМАТ ВВОДА

Строка с текстом, который нужно перевести, без знаков препинания.
Строка с названием языка, с которого нужно перевести и, через запятую, названием языка, на который нужно перевести.
Ссылка на страницу словаря, где есть колонка слов на языке страны (с которого надо перевести) и родном языке Васи (на который надо перевести).
ФОРМАТ ВЫВОДА

Строка с переводом.
Страницу, анализируемую в открытом тесте, можно посмотреть здесь.

Пояснение к примеру 1: артикль the не перевёлся, так как в таблице не был указан перевод, и в выводе нет ни перевода этого слова, ни лишнего пробела между “это” и “столица”.

Пояснение к примеру 2: одна и та же страница может использоваться для перевода между двумя языками в любую сторону, например, и с английского на русский, и с русского на английский.


При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
'''

import requests
from bs4 import BeautifulSoup

my_list = []
langs = []
t = input()
t = t.split(' ')
l = input()
l1 = []
l2 = []
output = []
weblink = input()

site = requests.get(weblink)
site.encoding = 'utf-8'
soup = BeautifulSoup(site.text, 'lxml')

for link in soup.find_all('th'):
    langs.append(link.get_text())

for link in soup.find_all('td'):
    my_list.append(link.get_text())

for i in range (0, len(my_list)):
    if i % 2 == 0:
        l1.append(my_list[i])
    else:
        l2.append(my_list[i])

if l == langs[0] + ',' + langs[1]:
    for i in range (0, len(t)):
        if t[i] in l1:
            output.append(l2[l1.index(t[i])])
    
if l == langs[1] + ',' + langs[0]:
    for i in range (0, len(t)):
        if t[i] in l2:
            output.append(l1[l2.index(t[i])])

output = list(filter(None, output))

print(" ".join(output))
        
        
        


    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

