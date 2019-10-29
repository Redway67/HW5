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
     5.  посмотреть только папки 
     6.  посмотреть только файлы  
     7.  просмотр информации об операционной системе 
     8.  создатель программы 
     9.  играть в викторину "День рождение русских писателей"
     10. мой банковский счет 
     11. смена рабочей директории
     12. выход 
     """)
    choice = input('>')
    if choice == '1':  # создать папку
        dir_name = input("Введите имя новой папки: ")
        os.mkdir(dir_name)

    elif choice == '2': # удаление файла/папки (без обработки ошибок)
        del_name = input('Введите имя удаляемого файла или папки:')
        if os.path.isdir(del_name):
            os.rmdir(del_name)
        elif os.path.isfile(del_name):
            os.remove(del_name)
        else:
            print('Неизвестное имя')

    elif choice == '3':
        print('3')

    elif choice == '4':  # просмотр содержимого рабочей директории
        print(os.listdir(path='.'))

    elif choice == '5':  # посмотреть только папки
        dirs_view = [d for d in os.listdir('.') if os.path.isdir(d)]
        print(dirs_view)

    elif choice == '6':  # посмотреть только файлы
        files_view = [f for f in os.listdir('.') if os.path.isfile(f)]
        print(files_view)

    elif choice == '7':  # просмотр информации об операционной системе
        print(f' Операционная система: {os.name}')

    elif choice == '8':  # создатель программы
        print('**************************************')
        print('*   Пушкин Александр Сергеевич  (c)  *')
        print('**************************************')

    elif choice == '9':  # играть в викторину "День рождения русских писателей"
        quiz()

    elif choice == '10':
        print('10')

    elif choice == '11':
        print('11')

    elif choice == '12':  # выход
        print('До новых встреч')
        break
    else:
        print('Неверный пункт меню')