'''
Диктант
Учитель составляет диктант, который должен проверять, как хорошо ученики усвоили новое правило правописания. Напишите программу, которая будет проверять, сколько слов на заданное правило в диктанте. 

ФОРМАТ ВВОДА 

На первой строке — буквосочетания, которые должны встречаться в словах диктанта, разделённые пробелом. 
На второй — текст диктанта: все предложения набраны строчными буквами, без заглавных. 
Гарантируется, что каждое слово не содержит двух или более различных проверяемых буквосочетаний. 
ФОРМАТ ВЫВОДА 

Одно число — сколько слов в тексте диктанта содержат нужные буквосочетания.
'''

count = 0

input1 = input()
input2 = input()

input2_fix = input2.replace(".", "") 

words = input2.split(" ")
sounds = input1.split(" ")
for i in range (0, len(words)):
    for j in range (0, len(sounds)):
        if sounds[j] in words[i]:
            count+=1

print(count)

            
        



            

