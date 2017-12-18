def dance(moves, programs):
	for move in moves:
		if move[0] == 's':
			programs = programs[-int(move[1:]):] + programs[:-int(move[1:])]
		elif move[0] == 'x':
			ind_1 = int(move.split('/')[0][1:])
			ind_2 = int(move.split('/')[1])
			programs[ind_1], programs[ind_2] = programs[ind_2], programs[ind_1]
		elif move[0] == 'p':
			
			ind_1 = programs.index(move.split('/')[0][1:])
			ind_2 = programs.index(move.split('/')[1])
			
			programs[ind_1], programs[ind_2] = programs[ind_2], programs[ind_1]

	return programs

## Read file
with open('./input.txt') as file:
	moves = file.read().strip().split(',')
## Define list programs
programs = bytearray('abcdefghijklmnop')
## Compute one dance
print 'Part one: final order is {:s}'.format(dance(moves, programs))

###### Part two
## Redefine programs
programs = bytearray('abcdefghijklmnop')
original_programs = bytearray('abcdefghijklmnop')
## Look for period of the dance
for i in range(int(1e9)):
	programs = dance(moves, programs)
	if programs == original_programs:
		period = i+1
		break
print 'The period is {:d}'.format(period)
## Compute only the remainder of 1 billion / period
programs = bytearray('abcdefghijklmnop')
for i in range(int(1e9%period)):
	programs = dance(moves, programs)
print programs
