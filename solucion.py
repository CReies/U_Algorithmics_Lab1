with open('./inputs/Entrada-800.txt', 'r') as file:
	lines = file.readlines()
	input800 = [line.strip() for line in lines]

with open('./inputs/Entrada-8000.txt', 'r') as file:
	lines = file.readlines()
	input8000 = [line.strip() for line in lines]

with open('./inputs/Entrada-80000.txt', 'r') as file:
	lines = file.readlines()
	input80000 = [line.strip() for line in lines]

print(input800)
print(input8000)
print(input80000)