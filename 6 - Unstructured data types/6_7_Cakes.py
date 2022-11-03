'''
Торты в инстаграме
Леонид печет торты и ведет профессиональный аккаунт в Instagram. Он хочет собрать статистику, сколько уникальных пользователей оставили комментарии к его постам на прошлой неделе. Кроме того, у Леонида есть список спам-аккаунтов, и если комментарий оставлен с такого аккаунта, то Леонид его не учитывает. Напишите программу, которая поможет Леониду. 

ФОРМАТ ВВОДА

Сначала вводятся аккаунты, с которых Леониду написали комментарии.
Каждый аккаунт вводится на новой строке, когда комментарии заканчиваются, вводится слово END. 
Далее вводятся спам-аккаунты, среди них могут быть те, которые не оставляли на прошлой неделе комментариев. 
Каждый аккаунт вводится на новой строке, когда комментарии заканчиваются, вводится слово END. 
ФОРМАТ ВЫВОДА

Целое число — количество уникальных не спам-аккаунтов, которые написали комментарии Леониду.
'''

accs = []
spam = []
newlist = []
count = 0

while True:
    string = input()
    if string == "END":
        break
    else:
        accs.append(string)

while True:
    string = input()
    if string == "END":
        break
    else:
        spam.append(string)
        
for i in accs:
  if i not in newlist:
    newlist.append(i)

for i in range (0, len(newlist)):
    if not (newlist[i] in spam):
        count+=1

print(count)


    

            
        








            
        



            
