'''
Ежемесячные траты
Вася заметил, что с каждым месяцем у него все хуже получается откладывать деньги на новый ноутбук. Он подумал, что это может произойти по той причине, что с каждым месяцем он тратит все больше и больше. Проверьте, действительно ли в каждый следующий месяц Вася тратил больше, чем в предыдущий.

ФОРМАТ ВВОДА

Целые неотрицательные числа, не превосходящие 1 миллион, каждое с новой строки, затем отрицательное число, показывающее конец ввода. 
ФОРМАТ ВЫВОДА

True, если в каждый следующий месяц Вася тратил больше, чем в предыдущий (без учета последнего введенного числа, означающего конец ввода), и False в противном случае. 
 Если были введены расходы всего за ноль или один месяц, ответ True.
'''

answer = True
money_spent = int(input())

if money_spent < 0:
    print(answer)
    
else:
    while True:
        previous_value = money_spent
        money_spent = int(input())
        if money_spent < 0:
            break
        if money_spent <= previous_value:
            answer = False
    print(answer)