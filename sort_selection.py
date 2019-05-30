# Выборкой

from random import randint

N = 10

_list = [randint(1, 99) for i in range(N)]

print(_list)

def selection(data_list):
    for i in range(N):
        m = i
        j = i + 1
        while j < N:
            if data_list[j] < data_list[m]:
                m = j
            j = j + 1
        # Обмен значениями
        data_list[i], data_list[m] = data_list[m], data_list[i]
    return data_list

print(selection(_list)) 