"""
Модуль account

Фунция my_account()
Запускает операции по счету
"""
import os
import pickle
import json

FILE_TOTAL = 'total.dat'
FILE_PURCHASES = 'purchases.json'



def add_money():
    add_sum = int(input('Ввести сумму на сколько пополнить счет:'))
    return add_sum


def buying(sum_account, purchases):
    sum_purchase = int(input('Ввести сумму покупки:'))
    if sum_purchase <= sum_account:
        purchase = input('Ввести название покупки:')
        purchases[purchase] = sum_purchase
    else:
        print('   НЕДОСТАТОЧНО СРЕДСТВ НА СЧЕТЕ!!!')
        sum_purchase = 0
    return sum_purchase


def history(purchases):
    if bool(purchases):
        print('   ПОКУПКИ:')
        for key in purchases:
            print(f'   {key} , цена: {purchases[key]}')
    else:
        print('   ПОКУПОК НЕТ !!!')
    return


def my_account():
    # инициализируем total из файла
    if os.path.exists(FILE_TOTAL):
        with open(FILE_TOTAL, 'rb') as f:
            total = pickle.load(f)
    else:
        total = 0

    # инициализируем покупки
    if os.path.exists(FILE_PURCHASES):
        with open(FILE_PURCHASES, 'r', encoding='UTF-8') as fj:
            purchases = json.load(fj)
    else:
        purchases = {}

    while True:
        print(f'   НА СЧЕТУ: {total} р.')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню')
        if choice == '1':
            total += add_money()
        elif choice == '2':
            total -= buying(total, purchases)
        elif choice == '3':
            history(purchases)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

    # сохраняем total в файл
    with open(FILE_TOTAL, 'wb') as f:
        pickle.dump(total, f)

    # сохраняем покупки
    with open(FILE_PURCHASES, 'w', encoding='UTF-8') as fj:
        json.dump(purchases, fj)

    return
