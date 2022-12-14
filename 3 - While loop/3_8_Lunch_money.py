'''
Траты на обеды
Вася каждый месяц придерживался разного режима питания, а потом решил выяснить, в какой месяц у него были самые дешевые обеды. Он посчитал и записал затраты на питание за последние несколько месяцев. Вычислите, какое наименьшее количество рублей в месяц Вася потратил на обеды.

ФОРМАТ ВВОДА

Целые неотрицательные числа, не превосходящие 1 миллион, каждое с новой строки, затем отрицательное число, показывающее конец ввода. 
ФОРМАТ ВЫВОДА

Число, равное наименьшему введенному числу (не считая последнего, означающего конец ввода).
'''

count = 0
minimal = 1000001
while True:
    money_spent = int(input())
    if money_spent < 0:
        break
    elif money_spent < minimal:
        minimal = money_spent

print(minimal)
