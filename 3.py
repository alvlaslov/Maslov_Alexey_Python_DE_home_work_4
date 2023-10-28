"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список"""

"""
Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег

"""

import decimal

amount = decimal.Decimal(0)
operation_count = 1
wealth_sum = decimal.Decimal(5_000_000)
wealth_tax_rate = decimal.Decimal(10) / decimal.Decimal(100)
multiple_number = 50
lower_limit_withdraw = decimal.Decimal(30)
upper_limit_withdraw = decimal.Decimal(600)
tax_withdraw = decimal.Decimal(15) / decimal.Decimal(1_000)
percent_loyal = decimal.Decimal(3) / decimal.Decimal(100)
operations = []


def main():
    global amount
    global operation_count
    while True:
        s = input('Choose operation:\n 1 - deposit\n 2 - withdraw\n 3 - exit\n Input:  ')
        if s not in ('1', '2', '3'):
            continue
            print_amount()

        if s == '1':
            deposit()
        elif s == '2':
            withdraw()
        else:
            print_amount()
            break


def deposit():
    """
    Replenishment of the account according to the terms of the task
    """
    global amount
    global operation_count
    while True:
        d = int(input('Input amount multiple 50: '))
        if d % multiple_number != 0:
            print('Incoorent amount')
            wealth_tax()
            print_amount()
            continue
        wealth_tax()
        amount += d
        log_operations("+", d)
        print(operations)
        print_amount()
        if operation_count % 3 == 0:
            amount += add_percent(amount)
            print_amount()
        operation_count += 1
        break


def withdraw():
    """
    Withdrawal from the account according to the terms of the task
    """
    global amount
    global operation_count
    while True:
        w = int(input('Input amount multiple 50: '))
        if w % multiple_number != 0:
            print('Incoorent amount')
            wealth_tax()
            print_amount()
            continue
        if amount <= w + withdraw_percent(w):
            print('Not enought money. Please reduce amount')
            print_amount()
            continue
        if amount >= w + withdraw_percent(w):
            wealth_tax()
            print(f'Tax: {withdraw_percent(w)}')
            amount -= (w + withdraw_percent(w))
            log_operations("-", w)
            print(operations)
            print_amount()
        if operation_count % 3 == 0:
            amount += add_percent(amount)
            print_amount()
        operation_count += 1
        break


def add_percent(x):
    """
    Returns the interest for crediting
    :param x: decimal number
    :return: decimal number
    """
    global percent_loyal
    y = round(x * percent_loyal, 2)
    print(f'Loyalty program +{y}')
    return y


def withdraw_percent(x):
    """
    Returns interest for debiting
    :param x: decimal number
    :return: decimal number
    """
    global lower_limit_withdraw, lower_limit_withdraw, upper_limit_withdraw, upper_limit_withdraw
    y = x * tax_withdraw
    if y < lower_limit_withdraw:
        y = lower_limit_withdraw
    elif y > upper_limit_withdraw:
        y = upper_limit_withdraw
    return y


def wealth_tax():
    """
    Wealth tax write-off
    """
    global amount, wealth_tax_rate
    if amount > wealth_sum:
        print(f'wealth_tax: -{amount * wealth_tax_rate}')
        amount -= amount * wealth_tax_rate


def print_amount():
    """
    Displaying the amount on the account
    """
    global amount
    print(f'The amount on the account: {amount}')


def log_operations(x, y):
    """
    Logging into the list of deposit and withdrawal operations
    :param x: string - sing "+" for replenishment; sing "-" for withdrawals
    :param y: int number
    """
    global operations
    oper = [x, y]
    operations.append(oper)


if __name__ == '__main__':
    main()
