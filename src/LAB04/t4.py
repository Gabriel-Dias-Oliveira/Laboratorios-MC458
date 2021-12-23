# Tarefa 04: Ordenar valores em hexadecimal (em tempo linear!).

def get_accounts(number_operations):
    accounts = {}
    
    for x in range(number_operations):
        account_number = input()

        if not account_number in accounts.keys():
            accounts[account_number] = 1
        else:
            accounts[account_number] += 1

    return accounts

def get_ascii_position(digit):
    position = ord(digit) - ord('0')

    return (position - 7) if (position > 9) else position

def counting_sort(account_list, sorted_list, digit, number_of_elements, char_number=36):
    aux_list = []

    for x in range(char_number):
        aux_list.append(0)
    
    for x in range(number_of_elements):
        element = get_ascii_position(account_list[x][digit]) 
        aux_list[element] += 1

    for x in range(1, char_number):
        aux_list[x] += aux_list[x - 1]

    for x in range((number_of_elements - 1), -1, -1):
        element = get_ascii_position(account_list[x][digit]) 

        sorted_list[aux_list[element] - 1] = account_list[x]
        aux_list[element] -= 1

    return sorted_list

def radix_sort(accounts, number_digits=31):
    number_elements = len(accounts)

    for x in range(number_digits - 1, -1, -1):
        if accounts[0][x] != ' ':
            accounts = counting_sort(accounts, accounts.copy(), x, number_elements)

    return accounts

number_operations = int(input())
accounts = get_accounts(number_operations)

answer = radix_sort(list(accounts.keys()))

print(len(answer))

for account in answer:
    print(f'{account} {accounts[account]}')
