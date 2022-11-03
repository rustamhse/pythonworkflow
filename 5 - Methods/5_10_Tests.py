'''
Тесты
Петя решает тесты из контрольно-измерительных материалов и записывает ответы в виде четырехзначного номера вопроса и ответа на него в виде одной заглавной буквы (например, 4578А). Ответы разделяются запятой и пробелом. В конце задачника есть ответы на вопросы, приведенные в виде последовательности заглавных букв. Помогите Пете сравнить, верно ли он решил тест. 

ФОРМАТ ВВОДА

Список ответов через запятую и пробел. 
Строка — последовательность заглавных букв латинского алфавита с верными ответами.
ФОРМАТ ВЫВОДА

Две строки: 

"Ваш ответ: " и последовательность заглавных букв латинского алфавита. 
Если тест решен верно, выводится "Молодец! Все верно", а если неверно — "Тест решен неверно, правильный ответ: " и последовательность заглавных букв латинского алфавита правильного ответа.
'''

input1 = input().split(", ")
answer = ''
input2 = input()

for i in range(0, len(input1)):
    answer += input1[i][4]

print("Ваш ответ: " + answer)

if answer == input2:
    print("Молодец! Все верно")
else:
    print("Тест решен неверно, правильный ответ: " + input2)





            
        



            
