with open('input.txt') as file:
	numbers = file.read()

numbers = list(numbers)
total = 0
for k, element in enumerate(numbers):
	if k == 0:
		first = element
		continue
	if element == numbers[k-1]:
		total += int(element)
		
if element == first:
	total += int(element)
print total

##### Part two
total = 0
for k, element in enumerate(numbers):

	if element == numbers[(k+len(numbers)/2)%len(numbers)]:
		total += int(element)

print total
