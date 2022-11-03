'''
Регистрация на хакатон

На студенческий хакатон зарегистрировалось множество команд, и организаторы хотят вывесить их перечень на сайт. Помогите им отсортировать список названий команд по алфавиту. Обратите внимание, что регистр букв в названии команд не должен учитываться.

ФОРМАТ ВВОДА

Строка из названий команд, разделённых символом “точка с запятой”.

ФОРМАТ ВЫВОДА

Строка из названий команд, разделённых символом “точка с запятой”.
'''

string = input()
array = string.split(";")

sorted_list = sorted(array, key=str.casefold)

print(*sorted_list, sep = ';')



    

            
        








            
        



            

