with open('./inputs/Entrada-800.txt', 'r') as file:
	lines = file.readlines()
	input800 = [int(line.strip()) for line in lines]

with open('./inputs/Entrada-8000.txt', 'r') as file:
	lines = file.readlines()
	input8000 = [int(line.strip()) for line in lines]

with open('./inputs/Entrada-80000.txt', 'r') as file:
	lines = file.readlines()
	input80000 = [int(line.strip()) for line in lines]

import time

def bubble(input : list[int])-> {list[int],int}:
	now = time.time()
	for i in range(len(input)):
		for j in range(len(input)-1):
			if input[j] > input[j+1]:
				input[j], input[j+1] = input[j+1], input[j]
	return {'sortedList': input, 'time': time.time() - now}