# Tarefa 02: Solucionar um Problema de subsequência consecutiva máxima (SCM).
# para encontrar o melhor caminho para uma viajante.

def find_niceness_path(stopping_niceness, stopping_points):
    counter = 0
    i = j = k = MaxSeq = MaxSuf = 0

    while (counter < (stopping_points - 1)):
        if counter == 0:
            if stopping_niceness[counter] < 0:
                i = j = k = 0
                MaxSeq = MaxSuf = 0
            else:
                i = j = k = 1
                MaxSeq = MaxSuf = stopping_niceness[counter]
        else:
            if k == 0:
                k = counter + 1
            
            MaxSuf += stopping_niceness[counter]

            if MaxSuf > MaxSeq or (MaxSuf == MaxSeq and ((((counter + 1) - k) > (j - i))) or (k < i)): 
                i = k 
                j = counter + 1
                MaxSeq = MaxSuf
            elif MaxSuf < 0:
                MaxSuf = k = 0

        counter += 1

    return (i, j)

stopping_points = int(input())
stopping_niceness = [int(x) for x in input().split(" ")]

begin, end = find_niceness_path(stopping_niceness, stopping_points)

print(f'{begin} {end}')
