'''
Номер телефона
В компании Contoso решили поменять стандарт записей в телефонном справочнике, вместо телефонных номеров вида 18005550123 решили использовать номера вида +1(800) 555-01-23. Помогите секретарям компании записать номера в новом формате.

ФОРМАТ ВВОДА: 


Строка из 11 цифр телефонного номера, вида 12345678910

ФОРМАТ ВЫВОДА: 

Строка вида +1(234) 567-89-10
'''

array = input()
print("+" + array[0] + "(" + array[1] + array[2] + array[3] + ") " + array[4] + array[5] + array[6] + "-" + array[7] + array[8] + "-" + array[9] + array[10])



