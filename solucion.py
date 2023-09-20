import time

with open('./inputs/Entrada-800.txt', 'r') as file:
	lines = file.readlines()
	input800 = [int(line.strip()) for line in lines]

with open('./inputs/Entrada-8000.txt', 'r') as file:
	lines = file.readlines()
	input8000 = [int(line.strip()) for line in lines]

with open('./inputs/Entrada-80000.txt', 'r') as file:
	lines = file.readlines()
	input80000 = [int(line.strip()) for line in lines]


# The bubble method consist in a for loop inside another for loop, the inside loop is where the operations are made, it compares the current element with the next one, if the current element is bigger than the next one, it swaps them, and it does this until the list is sorted.
def bubble(input : list[int])-> {list[int],int}:
	now = time.time()
	for i in range(len(input)):
		for j in range(len(input)-1):
			if input[j] > input[j+1]:
				input[j], input[j+1] = input[j+1], input[j]
	return {'sortedList': input, 'time': time.time() - now}

# The selection method consist in a for loop inside another for loop, it finds the minimum element in the list and swaps it with the first element, then it finds the second minimum element and swaps it with the second element, and it does this until the list is sorted.
def selection(input : list[int])-> {list[int],int}:
	now = time.time()
	for i in range(len(input)):
		min = i
		for j in range(i+1, len(input)):
			if input[min] > input[j]:
				min = j
		input[i], input[min] = input[min], input[i]
	return {'sortedList': input, 'time': time.time() - now}

# The insertion method consist in 2 loops, the first one is a for loop that starts in the second element of the list, the second one is a while loop that compares the current element with the previous one, if the current element is smaller than the previous one, it swaps them, then compares it with the second previous element, and if is smaller, it swaps them, and it does this until the current element is bigger than the previous one, then it goes to the next element and does the same until the list is sorted.
def insertion(input : list[int])-> {list[int],int}:
	now = time.time()
	for i in range(1, len(input)):
		key = input[i]
		j = i - 1
		while j >= 0 and key < input[j]:
			input[j + 1] = input[j]
			j -= 1
		input[j + 1] = key
	return {'sortedList': input, 'time': time.time() - now}

