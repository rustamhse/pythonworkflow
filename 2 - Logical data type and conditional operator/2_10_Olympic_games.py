'''
Путевки на Олимпийские игры
Спортсмен Славик хочет завоевать путевки на Олимпийские игры для своей страны. Для этого он участвует в чемпионате мира и чемпионате Европы. Правила таковы: 

Чтобы гарантированно получить путевки на Олимпийские игры, нужно войти в топ-20 чемпионата мира И топ-16 чемпионата Европы (оба условия должны выполниться одновременно). При этом, если войти в топ-10 хотя бы одного из чемпионатов, страна получает сразу 2 путевки, а если войти в топ-2 хотя бы одного из чемпионатов, то 3.
Если условия из п. 1 не выполнены, но спортсмен вошел в топ-24 чемпионата мира ИЛИ топ-20 чемпионата Европы, он отправляется на дополнительные отборочные соревнования, где у него будет еще один шанс. 
В ином случае спортсмен не получает путевку на Олимпийские игры для своей страны. 
Напишите программу, которая определяет, завоевал ли Славик путевки на Олимпийские игры. 

ФОРМАТ ВВОДА 

Два целых положительные числа, каждое с новой строки — места Славика на чемпионате мира и чемпионате Европы соответственно. 
ФОРМАТ ВЫВОДА 

Если Славик завоевал путевки, вывести "Ура! Путевки на Олимпийские игры завоеваны!" и далее с новой строки вывести количество путевок. 
Если Славик проходит на дополнительный отбор, вывести "Нужно принять участие в дополнительных отборочных соревнованиях". 
Иначе вывести "К сожалению, в этот раз не удалось завоевать путевки на Олимпийские игры".
'''

a = int(input())
b = int(input())

if a <= 20 and b <= 16:
    if a <= 2 or b <= 2:
        print("Ура! Путевки на Олимпийские игры завоеваны!")
        print("3")
    elif a <= 10 or b <= 10:
        print("Ура! Путевки на Олимпийские игры завоеваны!")
        print("2")
    else:
        print("Ура! Путевки на Олимпийские игры завоеваны!")
        print("1")
        
elif a <= 24 or b <= 20:
    print("Нужно принять участие в дополнительных отборочных соревнованиях")

else:
    print("К сожалению, в этот раз не удалось завоевать путевки на Олимпийские игры")
