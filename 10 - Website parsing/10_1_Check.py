'''
Проверка работоспособности сайта

Вы пишете программу, которая помогает вам определить, работает ли сайт вашей компании или что-то идёт не так. Напишите программу, которая, получив ссылку, выводит строчку “IT WORKS!”, если страницу успешно удалось загрузить и “ERROR” в противном случае 
'''

import requests
request = requests.get(input())
if request.status_code == 200:
    print ("IT WORKS!")
else:
    print ("ERROR")        
    
    
    
        
        





    
    



    
    






        




    

            
        








            
        



            
