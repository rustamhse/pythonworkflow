'''
Сашина кофейня — 3
Саша открыла кофейню. Там продаются различные напитки в трех размерах — маленькие, средние и большие. Цены на эти напитки записаны в прайс-листе.

Каждый день бариста записывает, какие напитки он продал. Помогите Саше по записям баристы составить отчет о выручке за день.

ФОРМАТ ВВОДА

Файл-таблица price-list.csv, где на каждой строке записаны цены на какой-либо вид кофе: в первой колонке название вида кофе, далее в каждой колонке соответственно цены на маленький, средний и большой напиток.
Файл-таблица coffee-statistics-3.csv, где на каждой строке записана информация о проданном кофе: в первой колонке его вид, во второй — размер.
ФОРМАТ ВЫВОДА

Файл-таблица sale-statistics.csv в кодировке utf-8, где на каждой строке записана информация о выручке за каждый вид кофе: в первой колонке название, во второй — заработанная сумма.
Результат отсортируйте по названию напитков в алфавитном порядке.
Разделителем во всех таблицах служит точка с запятой.

В образце используются файлы coffee-statistics-3.csv, price-list.csv и sale-statistics.csv
'''

prices_dict = {}
coffee_dict = {}
with open('price-list.csv', encoding='utf-8') as infile:    
    for line in infile:
        price = line.replace('\n', '').split(';')
        prices_dict.update({f"{price[0]}": {'маленький': int(price [1]), 'средний': int(price[2]), 'большой': int(price[3])}})
#print(prices_dict)

with open('coffee-statistics-3.csv', encoding='utf-8') as infile:    
    for line in infile:
        coffee = line.replace('\n', '').split(';')
        coffee_dict.update({f"{coffee[0]}": 0})

coffee_dict = dict(sorted(coffee_dict.items(), key = lambda item: item[0]))
#print(coffee_dict)
with open('coffee-statistics-3.csv', encoding='utf-8') as infile:    
    for line in infile:
        coffee = line.replace('\n', '').split(';')
        coffee_dict.update({f"{coffee[0]}": int(coffee_dict.get(coffee[0]) + prices_dict.get(coffee[0]).get(coffee[1])
                                               )})##
import csv
with open("sale-statistics.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    for row in coffee_dict.keys():
        file_writer.writerow([f"{row}", f"{coffee_dict[row]}"])        
#print(coffee_dict)
    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

