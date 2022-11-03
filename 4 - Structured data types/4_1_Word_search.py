'''
Поиск слова
Вводится текст в две строки и число N. Определить, есть ли в тексте N-ое слово (нумеруя с 1) и вывести его. Если слова нет, вывести "Такого слова нет".

ФОРМАТ ВВОДА

Две строки и число N — целое и положительное 
ФОРМАТ ВЫВОДА

Строка
'''

string1 = input()
string2 = input()
N = int(input())
not_found = True
search = string1.split() + string2.split()
for i in range (0, len(search)):
    if i == N - 1:
        print(search[i])
        not_found = False
        
if not_found == True:
    print("Такого слова нет")