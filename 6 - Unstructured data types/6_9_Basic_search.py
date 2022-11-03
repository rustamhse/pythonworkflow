'''
Поиск книги
В переменной books хранится словарь, ключами которого являются названия книг, а значениями — их авторы.

Напишите программу, которая принимает на вход некоторую непустую строку и выводит все книги, для которых введенная строка содержится либо в названии, либо в имени автора. Поиск чувствителен к регистру ("Гарри" и "гарри" — разные запросы). Если совпадений нет, программа ничего не выводит.

ФОРМАТ ВВОДА

Непустая строка 
ФОРМАТ ВЫВОДА

Авторы и названия книг, удовлетворяющие условию, каждая пара на новой строке. 
'''

books = {   'Сильмариллион': 'Джон Толкин', 
            'Гарри Поттер и кубок огня': 'Джоан Роулинг', 
            'Неукротимая планета': 'Гарри Гаррисон', 
            'Человек без лица': 'Альфред Бестер', 
            "Алиса в стране чудес": "Льюис Кэрролл", 
            "Космическая Одиссея": "Артур Кларк", 
            "Дюна": "Фрэнк Герберт", 
            "Двадцать тысяч лье под водой": "Жюль Верн", 
            "Янки из Коннектикута при дворе короля Артура": "Марк Твен", 
            "Американские боги": "Нил Гейман", 
            "Хроники Амбера": "Роджер Желязны", 
            "Хроники Нарнии": "Клайв С. Льюис", 
            "Война миров": "Герберт Уэллс" } 
            
search_book = input()
for k, v in books.items():
    if search_book in k or search_book in v:
        print(f'{v}: {k}')




    

            
        








            
        



            
