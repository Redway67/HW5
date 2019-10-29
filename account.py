"""
Модуль account

Фунция my_account()
Запускает операции по счету
"""
purchases = {}


def first_choice():
    add_sum = int(input('Ввести сумму на сколько пополнить счет:'))
    return add_sum


def second_choice(sum_account):
    sum_purchase = int(input('Ввести сумму покупки:'))
    if sum_purchase <= sum_account:
        purchase = input('Ввести название покупки:')
        purchases[purchase] = sum_purchase
    else:
        print('   НЕДОСТАТОЧНО СРЕДСТВ НА СЧЕТЕ!!!')
        sum_purchase = 0
    return sum_purchase


def third_choice():
    if bool(purchases):
        print('   ПОКУПКИ:')
        for key in purchases:
            print(f'   {key} , цена: {purchases[key]}')
    else:
        print('   ПОКУПОК НЕТ !!!')
    return


def my_account():
    total = 0

    while True:
        print(f'   НА СЧЕТУ: {total} р.')
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню')
        if choice == '1':
            total += first_choice()
        elif choice == '2':
            total -= second_choice(total)
        elif choice == '3':
            third_choice()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return
