'''
Электронные адреса
Таисия обновляет в своем списке электронные адреса одногруппников, перед тем как сделать рассылку. Одногруппники в сообщениях пишут ей свой неиспользуемый электронный адрес и через пробел тот, на который надо его заменить. Таисия находит адрес в своем списке, и заменяет его на новый. 

ФОРМАТ ВВОДА

Почтовые адреса одногруппников, записанные у Таисии, через запятую 
Количество одногруппников, чей адрес надо заменить, целое неотрицательное число. 
Для каждого одногруппника считывается пара "{старый адрес} {новый адрес}", записанные через пробел. 
ФОРМАТ ВЫВОДА

В ответе нужно вывести итоговый список адресов, адреса записаны через точку с запятой
'''

input1 = input()
input2 = int(input())
emails = []
new_emails = []

original_emails = input1.split(",")

for i in range (0, input2):
    emails.append(input())

for i in range (0, len(original_emails)):
    check = False
    for j in range (0, len(emails)):
        temp = emails[j].split(" ")
        if original_emails[i] == temp[0]:
            new_emails.append(temp[1])
            check = True
    if check == False:
        new_emails.append(original_emails[i])
        
            
for i in range (0, len(new_emails)-1):
            print(new_emails[i], end=';')
            
print(new_emails[len(new_emails)-1], end='')

            
        



            

