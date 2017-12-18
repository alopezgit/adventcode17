## Puzzle input
steps = 356
## Part one
## Initialize buffer and position
circular_buffer = [0]
current_position = 0
for insert_value in range(1, 2018):
	## Compute current position using circular list
	current_position = (current_position + steps) % len(circular_buffer)
	## Insert after current position
	circular_buffer.insert(current_position+1, insert_value)
	## Advance one
	current_position += 1

value_after_2017 = circular_buffer[current_position+1]
print 'Part one: Value after 2017 is {:d}'.format(value_after_2017)

## Part two

## We need to compute 50000000 iterations, using a list would be really slow
## But we do not need the list, we save only the last value inserted after the 0
## 0 is always the first element of the list

current_position = 0
for insert_value in range(1, 50000000):
	## The value inserted is the same as the circular list length at that step
	current_position = (current_position + steps) % insert_value
	## If current_position is 0, the value inserted would be after the 0
	if current_position == 0:
		save_insert = insert_value
	current_position += 1
	if insert_value % 100000 == 0:
		print 'Computed {:d} iterations out of 50000000 ({:2f}%)'.format(insert_value, 100*insert_value/5e7)

print '\n########### Results ###########'
print 'Part one: Value after 2017 is {:d}'.format(value_after_2017)
print 'Part two: Value after 0 is {:d}'.format(save_insert)