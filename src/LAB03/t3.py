# Tarefa 03: Construir um algoritmo que faz o menor número de 'flips' (trocas de posições consecutivas) e devolver este valor..

def merge_sort(list, count):
    if len(list) > 1:
        middle = len(list) // 2

        left_list = list[:middle]
        right_list = list[middle:]
  
        count = merge_sort(left_list, count)  
        count = merge_sort(right_list, count)
  
        i = j = k = 0
  
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                count += ((len(left_list) - i))
                j += 1
                
            k += 1
  
        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1
  
        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

    return count

number_elements = int(input())
list = [int(x) for x in input().split(" ")]

print(merge_sort(list, 0))
