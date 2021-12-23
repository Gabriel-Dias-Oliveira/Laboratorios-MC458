# Tarefa 04: Utilizando programação dinâmica encontrar qual é o menor valor que deverá ser pago em um item, levando em consideração as notas fornecidas na entrada.

import math

def find_payment(money, item_value):
    payment_table = [math.inf for x in range(item_value+1)]
    size_money_list = len(money)
    payment_table[0] = 0
    start = 1
    
    while True:
        for pay_value in range(start, len(payment_table)):
            min_qtd = math.inf

            for current_money in range(0, size_money_list):
                if money[current_money] <= pay_value and payment_table[pay_value - money[current_money]] + 1 <= min_qtd:
                    min_qtd  = payment_table[pay_value - money[current_money]] + 1 
            
            payment_table[pay_value] = min_qtd 
            
        if (payment_table[len(payment_table) - 1] != math.inf):
            return (len(payment_table) - 1, payment_table[len(payment_table) - 1])

        start = len(payment_table)
        payment_table.append(math.inf)

item_value = int(input())
qtd_money = int(input())
money = [int(x) for x in input().split(" ")]

value, notes = find_payment(money, item_value)

print(f'{value} {notes}')
