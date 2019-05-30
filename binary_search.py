# Бинарный поиск

from random import randint

N = 20
array = [randint(1, 99) for i in range(N)]
array.sort()
print(array)

print('Input your number: ')
number = int(input())

if number in array:
    print(array.index(number))
else:
    print('Cannot find this number')