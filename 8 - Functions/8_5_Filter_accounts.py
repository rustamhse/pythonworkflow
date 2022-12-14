'''
Подписки в Инстаграме
Помогите блогеру Сене выбрать из подписок в инстаграме аккаунты с определенными размерами аудитории, чтобы отправить предложение о сотрудничестве. 

ТРЕБУЕМАЯ ФУНКЦИЯ 

Функция filter_accounts, которая принимает в качестве параметра словарь accounts, ключами которого являются адреса аккаунтов, а значениями — число подписчиков. 
Также функция принимает в качестве параметров целые числа min_followers и max_followers. 
Функция должна возвращать список адресов аккаунтов, где число подписчиков находится в промежутке между min_followers и max_followers включительно, адреса должны быть отсортированы в лексикографическом порядке.
В этой задаче вы только определяете функцию: не нужно считывать ввод и вызывать ее, мы сделаем это автоматически при проверке.
'''

def filter_accounts(accounts: dict, min_followers, max_followers):
    return list(filter(lambda x: min_followers <= accounts[x] <= max_followers, sorted(accounts)))
    
    






        




    

            
        








            
        



            

