'''
Сашина кофейня — 2
Саша открыла кофейню. Там продают капучино, латте и раф маленького, среднего и большого размера. Также в кофе могут добавить сироп. Для маленького используется 10 мл сиропа, для среднего — 20 мл, для большого — 30 мл.

Каждый день бариста ведет отчет о том, какие напитки он продал. Помогите Саше подсчитать анализ расхода сиропа для какого-либо вида кофе.

ФОРМАТ ВВОДА

Файл-таблица coffee-statistics-2.csv, где на каждой строке записана информация о проданном кофе: в первой колонке его вид, во второй — размер, в третьей — вкус добавленного сиропа (если есть).
Строка с названием вида кофе, для которого нужно провести подсчеты
ФОРМАТ ВЫВОДА

Файл-таблица syrups-statistics.csv в кодировке utf-8, где на каждой строке записана информация о расходе каждого сиропа: в первой колонке вкус сиропа, далее расход для введенного вида кофе. Например, "кленовый;90".
Результат отсортируйте по вкусу сиропа в алфавитном порядке.
Разделителем в таблицах служит точка с запятой.

В образце используются файлы coffee-statistics-2.csv и syrups-statistics.csv
'''

coffee_dict = {'капучино':60, 'латте': 60, 'раф':80}
price_dict = {'маленький': 10, 'средний': 20, 'большой': 30}
total = 0
syrops = set()
target = input()

with open('coffee-statistics-2.csv', encoding='utf-8') as infile: 
    for line in infile:
        coffee = line.replace('\n', '').split(';')
        syrops.add(coffee[-1])
        #print(coffee)
    syrops.remove('')
    syrops_dict = dict.fromkeys(syrops, 0)
    syrops_dict = dict(sorted(syrops_dict.items(), key = lambda item: item[0]))

with open('coffee-statistics-2.csv', encoding='utf-8') as infile:    
    for line in infile:
        coffee = line.replace('\n', '').split(';')
        if target == coffee[0]:
            for word in syrops_dict.keys():
                #print(word)
                if word == coffee[-1]:
                    #print(word)
                    for mult in price_dict.keys():
                        #print(coffee[1])
                        if mult == coffee[1]:
                            syrops_dict[word] = syrops_dict[word] + price_dict[mult]
                            #print(mult)
                            #total+=coffee_dict[word] * price_dict[mult]
#print(syrops_dict)


import csv

with open("syrups-statistics.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter = ";", lineterminator="\r")
    for row in syrops_dict.keys():
        file_writer.writerow([f"{row}", f"{syrops_dict[row]}"])
    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            

