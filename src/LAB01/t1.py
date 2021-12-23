# Solução sem utilização de métodos prontos da linguagem (ex: .index()).
# Tarefa 01: Comparação da eficiência de diferentes métodos de acesso a listas. 

def swap(number_list, initial_position, final_position):
    number_list[initial_position], number_list[final_position] = number_list[final_position], number_list[initial_position]

def complex_swap(number_list, start, item):
    number_list[start], number_list[start+1:item], number_list[item+1:] = number_list[item], number_list[start:item], number_list[item+1:]

def mtf(number_list, actions_list):
    cost = 0

    for action in actions_list:
        for item in range(len(number_list)):    
            if number_list[item] == action:
                complex_swap(number_list, 0, item)
                break

            cost += 1

        cost += 1

    return cost 

def trans(number_list, actions_list):
    cost = 0

    for action in actions_list:
        for item in range(len(number_list)):

            if number_list[item] == action and item == 0:
                break
            elif number_list[item] == action:
                swap(number_list, item, item - 1)
                break
            
            cost += 1
    
        cost += 1

    return cost  

def sort_item(number_list, frequency, item_position):
    start = 0
    
    for x in range(item_position, -1, -1):
        if frequency[number_list[x]] <= frequency[number_list[item_position]]:        
            start = x
    
    return start

def fc(number_list, actions_list):
    cost = 0
    frequency = dict()

    for item in number_list:
        frequency[item] = 0

    for action in actions_list:

        for item in range(len(number_list)):
            if number_list[item] == action:
                frequency[action] += 1
                start = sort_item(number_list, frequency, item)

                if (start != 0) or (start != (len(number_list) - 1)):
                    complex_swap(number_list, start, item)

                break

            cost += 1

        cost += 1

    return cost   

def bit(number_list, bit_list, actions_list):
    cost = 0

    for action in actions_list:
        for item in range(len(number_list)):

            if number_list[item] == action and bit_list[item] == 1:
                number_list[0], number_list[1:item], number_list[item+1:] = number_list[item], number_list[0:item], number_list[item+1:]
                bit_list[item] = 0
                bit_list[0], bit_list[1:item], bit_list[item+1:] = bit_list[item], bit_list[0:item], bit_list[item+1:]
                break
            elif number_list[item] == action:
                bit_list[item] = 1
                break
            
            cost += 1

        cost += 1

    return cost  

number_items = int(input())
number_list = [int(x) for x in input().split(" ")]
bit_list = [int(x) for x in input().split(" ")]
number_actions = int(input())
actions_list = [int(x) for x in input().split(" ")]
number_operations = []

print(mtf(number_list.copy(), actions_list))
print(trans(number_list.copy(), actions_list))
print(fc(number_list.copy(), actions_list))
print(bit(number_list.copy(), bit_list.copy(), actions_list))
