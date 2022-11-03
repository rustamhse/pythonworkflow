'''
Эта музыка будет вечной

Полина хочет познакомиться с музыкой новой группы, послушав какие-нибудь три её песни. Помогите Полине выбрать, указав три наиболее прослушиваемые песни группы по данным стриминговых сервисов.

ФОРМАТ ВВОДА

Строка с адресом страницы со статистикой.
Гарантируется, что количество воспроизведений каждой песни уникально и все названия песен уникальны, что песен в таблице больше, чем 3.
ФОРМАТ ВЫВОДА

3 строки с названиями песен, упорядоченными по рейтингу
Страницу, анализируемую в открытом тесте, можно посмотреть здесь.

При отправке задачи в функцию BeautifulSoup() нужно передать второй аргумент: 'lxml'.

Например, вместо кода soup = BeautifulSoup(page.text) нужно написать soup = BeautifulSoup(page.text, 'lxml')
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
        
def maxelements(list1):
    final_list = []
  
    for i in range(0, 3): 
        max1 = 0
          
        for j in range(len(list1)):     
            if list1[j] > max1:
                max1 = list1[j];
                  
        list1.remove(max1);
        final_list.append(max1)
          
    return final_list

my_list = []
output = []
weblink = input()
site = requests.get(weblink)
site.encoding = 'utf-8'
soup = BeautifulSoup(site.text, 'lxml')
for link in soup.find_all('td'):
    my_list.append(link.get_text())

converted = list(map(maybeMakeNumber, my_list))
max_ = maxelements(converted)
max_ = [str(x) for x in max_]

for num in max_:
    if num in my_list:
        print(my_list[my_list.index(num)-1])
        


    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

