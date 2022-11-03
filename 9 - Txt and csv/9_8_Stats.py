'''
Сашина кофейня — 1
Саша открыла кофейню. Цена на маленькие напитки в ней такая:

капучино или латте — 60 рублей
раф — 80 рублей
Кроме маленьких, в кофейне продаются средние и большие напитки. Средний дороже маленького в 2 раза, большой —  в 3 раза.

Каждый день бариста ведет отчет о том, какие напитки он продал. Помогите Саше подсчитать по отчету суммарную выручку за день.

ФОРМАТ ВВОДА

Файл-таблица coffee-statistics.csv, где на каждой строке записана информация о проданном кофе: в первой колонке его вид, во второй —  размер. Разделителем в таблице служит точка с запятой.
ФОРМАТ ВЫВОДА

Целое число — суммарная стоимость проданного кофе.
В примере использован файл coffee-statistics.csv
'''

coffee_dict = {'капучино':60, 'латте': 60, 'раф':80}
price_dict = {'маленький': 1, 'средний': 2, 'большой': 3}
total = 0

with open('coffee-statistics.csv', encoding='utf-8') as infile: 
    for line in infile:
        coffee = line.replace('\n', '').split(';')
        cost = 0
        #print(coffee)
        for word in coffee_dict.keys():
            #print(word)
            if word == coffee[0]:
                #print(word)
                for mult in price_dict.keys():
                    #print(coffee[1])
                    if mult == coffee[1]:
                        #print(mult)
                        total+=coffee_dict[word] * price_dict[mult]
print(total)
        
        





    
    



    
    






        




    

            
        








            
        



            

