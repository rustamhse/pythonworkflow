'''
Англо-русский словарь
В текстовом файле в произвольном порядке записаны английские слова и их перевод на русский язык. Отформатируйте файл для словаря, отсортировав слова в алфавитном порядке и сгруппировав их по буквам. 

ФОРМАТ ВВОДА

Текстовый файл words.txt, где на каждой строке записана пара слов в формате "<английское слово> -  <русский перевод>". Все слова записаны маленькими буквами.
ФОРМАТ ВЫВОДА

Текстовый файл dictionary.txt в кодировке utf-8, в следующем формате:
На отдельной строке записывается буква английского алфавита
Далее на отдельных строках записываются все английские слова, начинающиеся на эту букву, вместе с переводами в формате  "<английское слово> - <русский перевод>".
Буквы и слова должны быть отсортированы в алфавитном порядке. Записываться должны только те буквы, для которых во входном файле есть слова.

В образце используются файлы words.txt и dictionary.txt
'''

dick = {}
with open('words.txt', encoding='utf-8') as infile:
    for line in infile:
        line = line.split('\n')
        line = line[0].split(' - ')
        dick.update({line[0]:line[1]})     
        #print(dick)
dick = dict(sorted(dick.items(), key = lambda item: item[0]))
#print(dick)
keys = list(dick.keys())
#print(keys)
values = list(dick.values())
#print(values)

#print(keys[0][0])



with open('dictionary.txt', mode = 'w', encoding = 'utf-8') as outfile:
    temp = keys[0][0]
    print(temp, file = outfile)
    for word in range(len(keys)):
        if keys[word][0] == temp:
            print(f"{keys[word]} - {values[word]}", file = outfile)
        else:
            temp = keys[word][0]
            print(temp, file = outfile)
            print(f"{keys[word]} - {values[word]}", file = outfile)





#with open('dictionary.txt', encoding = 'utf-8') as outfile:
    #letter = dick[0]
    #for 




    
    



    
    






        




    

            
        








            
        



            

