'''
Электронная почта
Вводится N строк. Требуется определить, сколько в этих строках суммарно записано адресов электронной почты. Считаем, что только адреса электронной почты содержат @. 

ФОРМАТ ВВОДА

Число N 
N строк
ФОРМАТ ВЫВОДА

Целое число — ответ на задачу
'''

def CountSymbol(string):
    c = 0
    for i in range (0,len(string)):
        if string[i] == "@":
            c += 1
    return c

n = int(input())
count = 0

for i in range (0, n):
    count += CountSymbol(input())
    
print(count)

            
        



            

