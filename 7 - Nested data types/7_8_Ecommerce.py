'''
Товары на странице интернет-магазина

Мира выбирает новую мебель в онлайн-магазине, но, к сожалению, она ограничена в финансах. Пожалуйста, помогите ей выбрать, отсортировав все товары на странице от самых дорогих к самым дешёвым.

ФОРМАТ ВВОДА

Строки, состоящие из названия очередного товара и, через точку с запятой и пробел, его цены в рублях. Цена каждого товара — целое, положительное число.

После всех строк с названиями товаров идёт строка “конец”, которая означает окончание ввода.

Гарантируется, что все названия уникальны и все цены уникальны.

ФОРМАТ ВЫВОДА

Строки с названиями товаров, каждое название с новой строки, в порядке уменьшения цены товара.
'''

arr = []
costs = []
result = []

while True:
    string = input()
    if string == "конец":
        break
    else:
        arr.append(string)
        costs.append(int(string.split(";")[1]))

costs.sort(reverse = True)

for i in range (0, len(costs)):
    for j in range (0, len(arr)):
        if costs[i] == int(arr[j].split(';')[1]):
            result.append(arr[j].split(';')[0])

for i in result:
    print(i)




        




    

            
        








            
        



            
