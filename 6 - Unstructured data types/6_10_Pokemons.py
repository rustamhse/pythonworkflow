'''
Покемоны
Студент, который начал изучать программирование на Python, но пока не умеет работать со словарями, сохранил в виде списка названия параметров, которые есть у каждого вида покемонов (номер, название, тип, рост, вес). 

par_name = ['Номер', 'Имя', 'Тип', 'Рост', 'Вес'] (cкопируйте этот список себе в программу).

Значения параметров для своего любимого покемона он собирается ввести в том же порядке с клавиатуры. Напишите программу, которая принимает на вход эти значения и выводит словарь pokemon, хранящий информацию о покемоне в удобной форме: элементы списка par_name должны стать ключами, а введенные параметры любимого покемона — соответствующими ключам значениями. 

ФОРМАТ ВВОДА 

Значения параметров покемона из списка par_name в обозначенном порядке. 
Каждое значение вводится с новой строки. 
ФОРМАТ ВЫВОДА

Словарь pokemon, в котором элементы списка par_name стали ключами, а введенные параметры — значениями
'''

par_name = ['Номер', 'Имя', 'Тип', 'Рост', 'Вес']
par_input = []

for i in range (0, 5):
    par_input.append(input())
    
print(dict(zip(par_name, par_input)))



    

            
        








            
        



            

