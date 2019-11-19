import os
import shutil
import random
import errno

from victory import quiz
from account import my_account

FILE_LISTDIR = 'listdir.txt'


# декоратор
def frame(func):
    def inner(*args, **kwargs):
        print('*' * 39)
        result = func(*args, **kwargs)
        print('*' * 39)
        return result

    return inner


@frame
def author():
    # тернарный оператор
    author_name = 'Пушкин Александр Сергеевич  (c)' if random.random() > 0.5 else 'Лермонтов Михаил Юрьевич    (с)'
    print(f'*   {author_name}  *')
    return


@frame
def bye_bye():
    # тернарный оператор
    good_bye = '     GOOD BYE!!                ' if random.random() > 0.5 else '        ДОСВИДАНИЯ!!           '
    print(f'*   {good_bye}  *')
    return


def show_files():
    # генератор
    f_view = [f for f in os.listdir('.') if os.path.isfile(f)]
    return f_view


if __name__ == '__main__':
    while True:
        print("""
        ____________________
        Выберите пункт меню:
        ____________________
         1.  создать папку 
         2.  удалить (файл/папку)
         3.  копировать (файл/папку) 
         4.  просмотр содержимого рабочей директории 
         5.  сохранить содержимое рабочей директории в файл
         6.  посмотреть только папки 
         7.  посмотреть только файлы  
         8.  просмотр информации об операционной системе 
         9.  создатель программы 
         10. играть в викторину "День рождение русских писателей"
         11. Банковский счет 
         12. смена рабочей директории
         13. выход 
         """)
        choice = input('>')
        if choice == '1':  # создать папку
            dir_name = input("Введите имя новой папки: ")
            # обрабатываем ошибку
            try:
                os.mkdir(dir_name)
            except OSError as exc:
                print(f' Ошибка!!!  {exc}')

        elif choice == '2':  # удаление файла/папки
            del_name = input('Введите имя удаляемого файла или папки:')
            if os.path.isdir(del_name):  # удаляем папку
                os.rmdir(del_name)
            elif os.path.isfile(del_name):  # удаляем файл
                os.remove(del_name)
            else:
                print('Неизвестное имя')

        elif choice == '3':  # копирование файла/папки
            src_name = input('Введите что копируем:')
            src_name = os.path.join(os.getcwd(), src_name)
            dst_name = input('Введите куда копируем:')
            dst_name = os.path.join(os.getcwd(), dst_name)
            if os.path.isfile(src_name):  # копируем файл
                shutil.copy(src_name, dst_name)
            elif os.path.isdir(src_name):  # копируем папку
                shutil.copytree(src_name, dst_name)
            else:
                print('Неизвестное имя')

        elif choice == '4':  # просмотр содержимого рабочей директории
            print(os.listdir(path='.'))

        elif choice == '5':  # сохранить содержимое рабочей директории в файл
            with open(FILE_LISTDIR, 'w', encoding='UTF-8') as f:
                file_names = ', '.join([ff for ff in os.listdir('.') if os.path.isfile(ff)])
                f.write(f'files: {file_names} \n')
                dir_names = ', '.join([ff for ff in os.listdir('.') if os.path.isdir(ff)])
                f.write(f'dirs : {dir_names}')

        elif choice == '6':  # посмотреть только папки
            # генератор
            dirs_view = [d for d in os.listdir('.') if os.path.isdir(d)]
            print(dirs_view)

        elif choice == '7':  # посмотреть только файлы
            # генератор
            files_view = [f for f in os.listdir('.') if os.path.isfile(f)]
            print(files_view)

        elif choice == '8':  # просмотр информации об операционной системе
            print(f' Операционная система: {os.name}')

        elif choice == '9':  # создатель программы
            author()

        elif choice == '10':  # играть в викторину "День рождения русских писателей"
            quiz()

        elif choice == '11':
            my_account()

        elif choice == '12':  # смена рабочей директории
            print(f'{os.getcwd()}>')
            new_dir = input('Папка перехода: ')
            os.chdir(new_dir)
            print(f'{os.getcwd()}>')

        elif choice == '13':  # выход
            bye_bye()
            break
        else:
            print('Неверный пункт меню')
