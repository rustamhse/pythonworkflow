'''
Гонорар за статью
Соня пишет статью для журнала. Ее вознаграждение будет рассчитываться по хитрой формуле, в которой используются количество символов, количество слов и количество предложений в статье. Напишите программу, которая считает файл с Сониной статьей и посчитает все эти параметры.

Количество символов считается без учета символов перехода на новую строку. Словом считается любая последовательность символов, отделенная пробелами, необязательно состоящая из букв или цифр. Предложения в тексте могут разделяться точками, восклицательными и вопросительными знаками.

ФОРМАТ ВВОДА

Файл article.txt с текстом статьи. Текст может быть разделен на абзацы.
ФОРМАТ ВЫВОДА

Три строки вида:

Количество символов: <количество>
Количество слов: <количество>
Количество предложений: <количество>
В образце используется файл article.txt.
'''

text = ''
with open('article.txt', encoding= 'UTF-8') as infile:
    lines = infile.read()


for line in lines:
    text += line
symb = len(text) - text.count('\n')

lines = lines.replace('\n', ' ')
text = ''
for line in lines:
    text += line

words = []
almost = text.split(' ')
sentences = 0
for word in almost:
    if '?' in word or '.' in word or '!' in word or '!?' in word or '...' in word:
        sentences += 1
    if word != '' or word != '':
        words.append(word.strip(''))




print('Количество символов:', symb)
print('Количество слов:', len(words))
print('Количество предложений:', sentences)



    
    



    
    






        




    

            
        








            
        



            

