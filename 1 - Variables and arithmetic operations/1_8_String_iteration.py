'''
Приключения Алисы
Алиса, попав в Зазеркалье, увидела, что все слова написаны задом наперёд: вместо слова “МИР” написано “РИМ”, вместо “ГОД” — “ДОГ”. Помогите ей прочитать написанные тексты, написав программу, которая будет выводить слова в обратном порядке. Известно, что в строке, с которой работает программа, ровно 3 буквы.

ФОРМАТ ВВОДА:


Строка из трёх символов

ФОРМАТ ВЫВОДА:


Строка из трёх символов
'''

word = input()
print(word[2]+word[1]+word[0])


