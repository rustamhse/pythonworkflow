'''
Библиотека
У Жени есть список учебников, которые нужно взять в библиотеке, и соответствующие им идентификационные номера ISBN (книга и соответствующий ей номер находятся в двух списках на одной и той же позиции). Чтобы найти книгу в библиотеке, нужно назвать ее ISBN. Часть книг у Жени уже есть, и их брать в библиотеке не нужно. 

Напишите программу, которая принимает на вход список названий книг, затем список номеров ISBN, затем названия книг, которые уже есть у Жени, и выводит ISBN тех книг, которых еще нет. 

ФОРМАТ ВВОДА 

Точные названия книг из списка учебников, с соблюдением регистра, разделенные запятой и пробелом. 
ISBN книг из списка учебников, с соблюдением регистра, разделенные запятой и пробелом. 
Точные названия книг, которые есть у Жени, с соблюдением регистра, разделенные запятой и пробелом. 
ФОРМАТ ВЫВОДА 

ISBN тех книг, которых у Жени нет, каждый номер на новой строке
'''

input1 = input()
input2 = input()
input3 = input()

books = input1.split(", ")
ids = input2.split(", ")
my_books = input3.split(", ")

count_index = []

for i in range (0, len(books)):
    if books[i] in my_books:
        count_index.append(i)

for i in range (0, len(books)):
    if not (i in count_index):
        print(ids[i])
            

