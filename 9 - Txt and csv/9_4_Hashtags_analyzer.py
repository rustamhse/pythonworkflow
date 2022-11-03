'''
Анализ тегов Твиттера
В текстовом файле находится выгрузка постов из Твиттера, за некоторый период, в которых встречаются теги. Выясните, какие теги являлись более популярными, а какие менее, подсчитав количество употреблений каждого.

ФОРМАТ ВВОДА

Текстовый файл tweets.txt, в котором записана подборка постов из Твиттера, размеченных тегами. Тегом считается любое слово, начинающееся с '#'. Гарантируется, что все теги записаны маленькими буквами, и в них не встречаются знаки препинания.
ФОРМАТ ВЫВОДА

Текстовый файл tags.txt в кодировке utf-8, где каждый твит, использованный в файле tweets.txt, записан в формате "тег: <тег>, упоминаний: <кол-во упоминаний>". Каждый тег должен быть записан на отдельной строке, теги нужно отсортировать по количеству упоминаний от самого большого к самому маленькому
В образце используются файлы tags.txt и tweets.txt
'''

text = ''
with open('tweets.txt', encoding= 'UTF-8') as infile:
    lines = infile.read().replace('\n', ' ')
    
for line in lines:
    text += line    
splits = text.split(' ')
hashtags = []
for word in splits:
    if word.startswith('#'):
        hashtags.append(word)
print(hashtags)


new_values = {}

for value in hashtags:
    if value in new_values.keys():
        new_values[value] += 1
    else:
        new_values[value] = 1
    
new_values = sorted(new_values.items(), key = lambda kv: kv[1], reverse=True)  
print(new_values)

with open('tags.txt', mode = 'w') as outfile:
    for value in new_values:
        print(f"тег: {value[0]}, упоминаний: {value[1]}", file = outfile)




    
    



    
    






        




    

            
        








            
        



            

