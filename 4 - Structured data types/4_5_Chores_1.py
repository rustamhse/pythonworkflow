'''
Домашние дела - 1
Женя и Саша распределяют между собой домашние дела из общего списка, при этом стараясь поделить работу пополам: если в списке четное количество дел, то Женя делает первую половину, а Саша — вторую; если в списке нечетное число задач, то задачу, которая оказалась посередине, они делают вместе (она попадает в список задач и Саши, и Жени). 

Напишите программу, которая принимает на вход общий список дел и выводит списки дел для Саши и Жени. 

ФОРМАТ ВВОДА

Общий список дел, перечисленных через запятую и пробел. 
ФОРМАТ ВЫВОДА 

Два списка через запятую и пробел: сначала список дел Жени, затем список дел Саши каждый список выводится с новой строки.
'''

tasks = input()
search = tasks.split(", ")
answer1 = []
answer2 = []

if len(search) % 2 != 0:   
    for i in range (0, len(search) // 2 + 1):
            answer1.append(search[i])
    for i in range (len(search) // 2, len(search)):
            answer2.append(search[i])
            
else:
    for i in range (0, len(search) // 2):
            answer1.append(search[i])
    for i in range (len(search) // 2, len(search)):
            answer2.append(search[i])
            
for i in range (0, len(answer1)-1):
            print(answer1[i], end=', ')
            
print(answer1[len(answer1)-1], end='')

print()
            
for i in range (0, len(answer2)-1):
            print(answer2[i], end=', ')
            
print(answer2[len(answer2)-1], end='')
