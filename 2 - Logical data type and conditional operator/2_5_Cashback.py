'''
Кэшбэк
Банк предложил Арсению следующие условия по кэшбэку: 1% на все покупки, 3% на покупки в категории "продукты", 5% в категории "аптеки". Помогите Арсению определить по данным о его покупке, какой кэшбэк он получит. 

ФОРМАТ ВВОДА 

Строка — название категории покупки Далее целое положительное число — стоимость покупки 
ФОРМАТ ВЫВОДА 

Вещественное положительное число — кэшбэк Арсения за покупку
'''

a = input()
cash = int(input())

if a == "аптеки":
    cashback = 0.05 * cash
elif a == "продукты":
    cashback = 0.03 * cash
else:
    cashback = 0.01 * cash
    
print(cashback)