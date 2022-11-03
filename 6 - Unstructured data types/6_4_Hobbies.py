'''
Запись на кружки
В классе каждый ученик должен выбрать себе два кружка из трёх. Ведущий каждого кружка принёс классному руководителю неупорядоченные имена учеников, записанным к нему. Каждый ученик выбрал два кружка, но некоторые ученики решили схитрить и записались на все кружки сразу. Вычислите, сколько их. 

 ФОРМАТ ВВОДА

На первой строке — список учеников в первом кружке через запятую и пробел; 
на второй — список учеников во втором кружке через запятую и пробел; 
на третьей — список учеников в третьем кружке через запятую и пробел. 
 ФОРМАТ ВЫВОДА

Число, количество учеников, записанных сразу на три кружка
'''

a = input().split(", ")
b = input().split(", ")
c = input().split(", ")

common = set(a) & set(b) & set(c)

print(len(common))

            
        








            
        



            
