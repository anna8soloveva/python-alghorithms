# Быстрая

import random
from random import randint


N = 10
_list = [randint(1,99) for i in range(N)]

print(_list)


# Метод сортировки
def qsort(arglist, start, end):
    if start >= end: return
    l, r = start, end
    x = arglist[(l+r)//2]
    while l <= r:
        while arglist[l] < x: l += 1 # разделение
        while arglist[r] > x: r -= 1
        if l <= r:
            arglist[l], arglist[r] = arglist[r], arglist[l]
            l += 1
            r -= 1
        qsort(arglist, start, r) # рекурсивные вызовы
        qsort(arglist, l, end)


qsort(_list, 0, N-1)
print('Отсортированный список:')
print(_list)