'''
Комментаторы в инстаграме

Три друга — Петя, Вася и Миша хотят узнать, у кого из них больше уникальных комментаторов в инстаграме. У каждого из них есть список, куда они выписали логины всех своих комментаторов, но в этом списке логины могут повторяться. Помогите им, посчитав только уникальных комментаторов каждого. 

ФОРМАТ ВВОДА

Строки, где указано имя друга (Вася, Миша или Петя) и, через двоеточие, указан логин в сети Инстаграм комментатора. Каждая на новой строке.

После всех строк идёт строка “конец”, которая означает окончание ввода.

ФОРМАТ ВЫВОДА

3 строки вида “У Пети 3 уникальных комментатора.” для Васи, Миши и Пети. 

Строки выводят в алфавитном порядке, в котором идут имена (Вася, Миша, Петя). 

Также последняя буква имени должна быть изменена на 'и'.
'''

res = {}
for line in iter(input, 'конец'):
    k, v = line.split()
    res[k] = res.get(k, set()) | {v}
print('\n'.join(map(lambda x: f'У {x[:-2]}и {len(res[x])} уникальных комментатора.', sorted(res))))



        




    

            
        








            
        



            

