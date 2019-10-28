import os
from victory import quiz


while True:
    print("""
    ____________________
    Выберите пункт меню:
    ____________________
     1.  создать папку 
     2.  удалить (файл/папку)
     3.  копировать (файл/папку) 
     4.  просмотр содержимого рабочей директории 
     5,  посмотреть только папки 
     6.  посмотреть только файлы  
     7.  просмотр информации об операционной системе 
     8.  создатель программы 
     9.  играть в викторину "День рождение русских писателей"
     10. мой банковский счет 
     11. смена рабочей директории
     12. выход 
     """)
    choice = input('>')
    if choice == '1':
        dir_name = input("Введите имя новой папки: ")
        os.mkdir(dir_name)
    elif choice == '2':
        print('2')
    elif choice == '3':
        print('3')
    elif choice == '4':
        cwd = os.getcwd()
        print(os.listdir(path=cwd))
    elif choice == '5':
        print('five')
    elif choice == '6':
        print('6')
    elif choice == '7':
        print(f' Операционная система: {os.name}')
    elif choice == '8':
        print('**************************************')
        print('*   Пушкин Александр Сергеевич  (c)  *')
        print('**************************************')
    elif choice == '9':
        quiz()
    elif choice == '10':
        print('10')
    elif choice == '11':
        print('11')
    elif choice == '12':
        print('До новых встреч')
        break
    else:
        print('Неверный пункт меню')
