# Tarefa 06: Construir um algoritmo guloso que calcula o melhor tempo para que um grupo de pessoas (com tempo de travessia diferentes) cruzem uma ponte.
# apenas duas pessoas podem cruzar a ponte por vez e alguém precisa voltar para devolver a "lanterna" para o restante do grupo.

def minimum_time(time_list):
	total_of_people = len(time_list)
	total_time = first_try = second_try = 0

	while total_of_people > 3:
		# Take the 2 fastest person | Take the 2 slowest person.
		first_try = (2 * time_list[1]) + time_list[0] + time_list[total_of_people - 1] 
		# Take the 2 fastest is not always the best aproach, the second guy can be very slow.
		second_try = (2 * time_list[0]) + time_list[total_of_people - 1] + time_list[total_of_people - 2] 

		total_time += min(first_try, second_try) 

		total_of_people -= 2

		if total_of_people != 3:
			total_time += time_list[total_of_people - 1]
		else: 
			total_time += time_list[0] + time_list[1] + time_list[2]

	return total_time

people_number = int(input())
time_list = [int(x) for x in input().split(" ")]

print(minimum_time(time_list))
