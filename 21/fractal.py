import copy
import itertools

def flip(pattern):
	## Performs a flip on the pattern
	for i in range(len(pattern)):
		pattern[i][0], pattern[i][-1] = pattern[i][-1], pattern[i][0]
	return pattern

def rotate(pattern):
	## Rotates the patern by 90 degrees
	rotated_pattern = [['' for i in range(len(pattern))] for i in range(len(pattern))]
	for i in range(len(pattern)):
		rotated_pattern[0][i] = pattern[i][0]
		rotated_pattern[1][i] = pattern[i][1]
		if len(pattern) == 3:
			rotated_pattern[2][i] = pattern[i][2]
	return rotated_pattern

def augment_list(list_patterns):
	## Takes a list of patterns and outputs a dictionary with all the rotations and flips
	dict_pattern = {}
	for pattern in list_patterns:
		key = ''.join(sum(pattern['original'], []))
		dict_pattern[key] = copy.deepcopy(pattern['new'])
		for n_flip_rotate in range(7):
			if n_flip_rotate % 2 == 0:
				pattern['original'] = flip(pattern['original'])
			else:
				pattern['original'] = rotate(pattern['original'])
			key = ''.join(sum(pattern['original'], []))
			dict_pattern[key] = copy.deepcopy(pattern['new'])
	return dict_pattern

def check_pattern(square):
	## Outputs the new pattern
	key = ''.join(sum(square, []))
	new_pattern = [x[:] for x in dict_pattern[key]]
	return new_pattern

def divide_squares(input_puzzle):
	## Divides the input in squares and looks for the new pattern
	if len(input_puzzle)%2 == 0:
		size_square = 2
	else:
		size_square = 3
	output_patterns = []
	for i in range(len(input_puzzle)/size_square):
		for j in range(len(input_puzzle)/size_square):
			
			square = map(lambda x: x[size_square*j:size_square*(j+1)], input_puzzle[size_square*i:size_square*(i+1)])
			new_pattern = check_pattern(square)
			for n_row, row in enumerate(new_pattern):
				if (size_square+1)*i+n_row < len(output_patterns):
					output_patterns[(size_square+1)*i+n_row]+= row
				else:
					output_patterns.append(row)

	return output_patterns

input_puzzle = ['.#.',
				'..#',
				'###']
input_puzzle = map(lambda x: list(x), input_puzzle)


def split_string(pattern):
	original = map(lambda x: list(x), pattern.split(' =')[0].split('/'))
	new = map(lambda x: list(x), pattern.split('> ')[-1].strip("\n").split('/'))
	return {'original': original, 'new': new}

with open('input.txt') as file:
	## We form a dictionary with all the possible flips and rotations
	dict_pattern = augment_list(map(lambda x: split_string(x), file.readlines()))

for iteration in range(1, 19):
	input_puzzle = divide_squares(input_puzzle)
	if iteration == 5:
		print 'Part one: after 5 iterations there are {:d} pixels on.'.format(sum(map(lambda x: x.count('#'), input_puzzle)))

print 'Part two: after 18 iterations there are {:d} pixels on.'.format(sum(map(lambda x: x.count('#'), input_puzzle)))