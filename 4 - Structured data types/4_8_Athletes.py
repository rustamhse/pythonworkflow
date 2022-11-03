'''
Спортсмены
Через пробел в одну строку вводится список спортсменов в том порядке, в каком они заняли места на соревновании. Далее через пробел в одну строку вводятся места спортсменов. Определите по местам, какие спортсмены их заняли. 

ФОРМАТ ВВОДА 

Две строки. Первая строка с именами через пробел. Вторая строка с целыми положительными числами через пробел. 
ФОРМАТ ВЫВОДА

Для каждого числа из ввода вывести строку формата "<место> занял <спортсмен>", либо строку формата "<место> никто не занял", если спортсмена на таком месте в введенном списке нет.
'''

sp = input().split()
nms = list(map(int, input().split()))
print('\n'.join((f'{i} место занял {sp[i - 1]}' if i <= len(sp) else f'{i} место никто не занял' for i in nms)))

            
