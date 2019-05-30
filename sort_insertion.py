# Вставками

from random import randint

N = 10

_list = [randint(1, 99) for i in range(N)]

print(_list)

def insertion(data_list):
	# Обрабатываем список
	for i in range(N):
		# j всегда меньше i на единицу вначале цикла
		j = i - 1 
		# key - запоминаем текущий элемент в списке (элемент на позиции i)
		key = data_list[i]
		# Пока j больше либо равен 0 и предыдущий элемент больше текущего элемента
		# данный код будет выполняться
		# Движемся по списку влево до тех пор, пока не найдем значение, которое меньше либо
		# запомненного (key) и после этого значения вставляем key
		while j >= 0 and data_list[j] > key:
			# На позицию j+1 ставим предыдущий элемент
			data_list[j+1] = data_list[j]
			# Уменьшаем j на единицу
			j = j - 1
		# Ставим на позицию j+1 запомненный элемент
		data_list[j+1] = key
	# Возвращаем отсортированный список
	return data_list

print(insertion(_list))