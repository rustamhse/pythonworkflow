'''
Повышенная стипендия - 2
Повышенная стипендия за отличную учебу равна 20000. Вася устроился на работу и решил по возможности откладывать деньги со стипендии на новый ноутбук. Иногда ему не хватает зарплаты, а иногда даже остаются лишние деньги, которые он тоже откладывает. Каждый месяц, когда Вася откладывает деньги, он записывает отложенную сумму. Помогите Васе определить количество месяцев, когда он смог отложить на ноутбук всю стипендию.

ФОРМАТ ВВОДА

Целые неотрицательные числа, каждое с новой строки, затем отрицательное число, показывающее конец ввода. 
ФОРМАТ ВЫВОДА

Число, означающее количество месяцев, когда Вася отложил не менее 20 000 рублей в месяц.
'''

s = []
count = 0

while True:
    money_spent = int(input())
    s.append(money_spent)
    if money_spent >= 20000:
        count += 1
    elif money_spent < 0:
        break

print(count)