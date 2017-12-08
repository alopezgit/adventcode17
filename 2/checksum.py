with open('input.txt') as file:
	numbers = file.read()

numbers = [i.split('\t') for i in numbers.split('\n')]
total = 0
for row in numbers:
	row = map(int, row)
	total += max(row) - min(row)
print total

## Part two
total = 0
for row in numbers:
	row = map(int, row)
	for k, element in enumerate(row):
		divide = [x % element for x in row]
		divide[k] += 1
		print divide
		if 0 in divide:
			total += row[divide.index(0)]/element
print total