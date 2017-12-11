with open('input.txt') as file:
	data = file.read()

garbage = 0
ignore = 0
data_clean = []
garbage_all = []

## We clean the data
for character in data:
	if ignore == 1:
		ignore = 0
		continue
	elif character == '!':
		ignore = 1
		continue
	elif character == '>':
		garbage = 0
		continue
	elif character == '<' and garbage == 0:
		garbage = 1
		continue
	if garbage == 0:
		data_clean.append(character)
	else:
		garbage_all.append(character)

## Compute sum
total_sum = 0
level = 0
for character in data_clean:
	if character == '{':
		level += 1
	if character == '}':
		total_sum += level
		level += -1

print total_sum

### Part two

print len(garbage_all)

