import os
import time 
import math

# ====== Inputs ====== #

# 800 lines input
with open('./inputs/Entrada-800.txt', 'r') as file:
	lines = file.readlines()
	input800 = [int(line.strip()) for line in lines]

# 8000 lines input
with open('./inputs/Entrada-8000.txt', 'r') as file:
	lines = file.readlines()
	input8000 = [int(line.strip()) for line in lines]

# 80000 lines input
with open('./inputs/Entrada-80000.txt', 'r') as file:
	lines = file.readlines()
	input80000 = [int(line.strip()) for line in lines]


# ====== Functions ====== #

# The bubble method consist in a for loop inside another for loop, the inside loop is where the operations are made, it compares the current element with the next one, if the current element is bigger than the next one, it swaps them, and it does this until the list is sorted.
def bubble(input : list[int])-> list[int]:
	for i in range(len(input)):
		for j in range(len(input)-1):
			if input[j] > input[j+1]:
				input[j], input[j+1] = input[j+1], input[j]
	return input

# The selection method consist in a for loop inside another for loop, it finds the minimum element in the list and swaps it with the first element, then it finds the second minimum element and swaps it with the second element, and it does this until the list is sorted.
def selection(input : list[int])-> list[int]:
	for i in range(len(input)):
		min = i
		for j in range(i+1, len(input)):
			if input[min] > input[j]:
				min = j
		input[i], input[min] = input[min], input[i]
	return input

# The insertion method consist in 2 loops, the first one is a for loop that starts in the second element of the list, the second one is a while loop that compares the current element with the previous one, if the current element is smaller than the previous one, it swaps them, then compares it with the second previous element, and if is smaller, it swaps them, and it does this until the current element is bigger than the previous one, then it goes to the next element and does the same until the list is sorted.
def insertion(input : list[int])-> list[int]:
	for i in range(1, len(input)):
		key = input[i]
		j = i - 1
		while j >= 0 and key < input[j]:
			input[j + 1] = input[j]
			j -= 1
		input[j + 1] = key
	return input

# The merge method consist in a recursive function that divides the list in 2 parts, then it calls itself with the left part and the right part, and it does this until the list is divided in single elements, then it starts to merge the lists, it compares the first element of the left list with the first element of the right list, if the first element of the left list is smaller, it adds it to the final list, and it does this until one of the lists is empty, then it adds the remaining elements of the other list to the final list, and it does this until the whole list is sorted.
def merge(input : list[int])-> list[int]:
	if len(input) > 1:
		mid = len(input) // 2
		left = input[:mid]
		right = input[mid:]
		merge(left)
		merge(right)
		i = j = k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				input[k] = left[i]
				i += 1
			else:
				input[k] = right[j]
				j += 1
			k += 1
		while i < len(left):
			input[k] = left[i]
			i += 1
			k += 1
		while j < len(right):
			input[k] = right[j]
			j += 1
			k += 1
	return input

# The quick method consist in a recursive function that first checks if the list has more than 1 element, if it has, it takes the first element as the pivot, then it creates 2 lists, one with the elements smaller than the pivot, and the other with the elements bigger than the pivot, then it calls itself with the left list and the right list, and it does this until the list is divided in single elements, then it starts to merge the lists, it adds the left list, then the pivot, and then the right list, and it does this until the whole list is sorted.
def quick(input):
	if len(input) <= 1:
		return input

	pivot = input[0]
	left = [x for x in input[1:] if x < pivot]
	right = [x for x in input[1:] if x >= pivot]
	return quick(left) + [pivot] + quick(right)

# ====== Interface ====== #

def printSeparator():
	print('\n====================\n')

def clearScreen():
	for i in range(os.get_terminal_size().lines):
		print('\n')

def pressEnter():
	input('Presione enter para continuar...')

def invalidOption():
	print('Opción inválida')
	pressEnter()
	clearScreen()

def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1, length = os.get_terminal_size().columns, fill = '█', printEnd = "\r"):
	percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	filledLength = int(length * iteration // total)
	bar = fill * filledLength + '-' * (length - filledLength)
	print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
	if iteration == total:
		print()

while True:
	clearScreen()
	print('Bienvenido al programa de ordenamiento de listas')

	printSeparator()

	print('Seleccione el método de ordenamiento que desea utilizar:')
	method = input('1. Burbuja\n2. Selección\n3. Inserción\n4. MergeSort\n5. QuickSort\n6. Salir\n')
	validMethods = ['1', '2', '3', '4', '5', '6']

	if method not in validMethods:
		invalidOption()
		continue

	printSeparator()

	print('Seleccione el tamaño de la lista que desea ordenar:')
	size = input('1. 800\n2. 8000\n3. 80000\n')
	validSizes = ['1', '2', '3']

	if size not in validSizes:
		invalidOption()
		continue

	printSeparator()

	print('Cuantas veces desea ordenar la lista para promediar? (max: 100)')
	times = int(input())
	maxTimes = 10000

	if times > maxTimes:
		print('El número de veces no puede ser mayor a ' + str(maxTimes))
		pressEnter()
		clearScreen()
		continue

	printSeparator()

	print('Desea ver la lista ordenada?')
	show = input('1. Si\n2. No\n') == '1'

	printSeparator()

	selectedMethod = None
	selectedInput = None

	if method == '1':
		selectedMethod = bubble
	elif method == '2':
		selectedMethod = selection
	elif method == '3':
		selectedMethod = insertion
	elif method == '4':
		selectedMethod = merge
	elif method == '5':
		selectedMethod = quick
	elif method == '6':
		break

	
	if size == '1':
		selectedInput = input800
	elif size == '2':
		selectedInput = input8000
	elif size == '3':
		selectedInput = input80000


	print('Ordenando lista...')

	printProgressBar(0, times, prefix = 'Progreso:', suffix = 'Completado', length = os.get_terminal_size().columns - 40)

	start = time.time()
	for i in range(times):
		selectedMethod(selectedInput)
		printProgressBar(i + 1, times, prefix = 'Progreso:', suffix = 'Completado', length = os.get_terminal_size().columns - 40)

	end = time.time()

	printSeparator()

	if show:
		printSeparator()
		print('Lista ordenada:')
		print(selectedMethod(selectedInput))
	else:
		print('Lista ordenada')

	printSeparator()

	print('Tiempo total: ' + str(end - start) + ' s')
	print('Tiempo promedio: ' + str((end - start) / times) + ' s')
	pressEnter()

