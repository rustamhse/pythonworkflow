'''
Рамона
Рамона Флауэрс каждую неделю красит волосы в новый цвет. Обязательное правило: цвет не должен использоваться в предыдущие три недели. Напишите программу, которая будет определять, может ли Рамона использовать какой-либо цвет. 

ФОРМАТ ВВОДА 

Три различных названия цвета, которые Рамона использовала ранее, каждое с новой строки. 
Далее с новой строки название цвета, в который Рамона хочет покраситься на этой неделе. 
ФОРМАТ ВЫВОДА 

Если Рамона может использовать цвет, выводится строка "Красимся!" 
Если Рамона не может использовать цвет, выводится строка "Нужен новый цвет!"
'''

a1 = input()
a2 = input()
a3 = input()
b = input()

if not ((b == a1) or (b == a2) or (b == a3)):
    print("Красимся!")
else:
    print("Нужен новый цвет!")