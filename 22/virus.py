from operator import add

def transform_dict(grid):
	## We form a dictionary, which is easier to modify
	dict_grid = {}
	for i, row in enumerate(grid): 
		for j, element in enumerate(row):
			dict_grid[str(i)+','+str(j)] = element
	return dict_grid

with open('./input.txt') as file:
	grid = map(lambda x: x.strip(), file.readlines())

position_virus = [(len(grid)-1)/2, (len(grid[0])-1)/2]
facing = 0
directions = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
grid = transform_dict(grid)
bursts = 0
infections = 0
while True:
	## Check if the element is in the dict
	key_grid = '{:d},{:d}'.format(position_virus[0], position_virus[1])
	if key_grid in grid:
		node = grid[key_grid]
	else:
		grid[key_grid] = '.'
		node = '.'
	if node == '.':
		facing = (facing - 1) % 4
		grid[key_grid] = '#'
		infections += 1
	elif node == '#':
		facing = (facing + 1) % 4
		grid[key_grid] = '.' 
	position_virus = map(add, position_virus, directions[facing])
	bursts += 1
	if bursts == 10000:
		break
print 'Part one: the number of infections is {:d}'.format(infections)


#### Part two ######
## Init as in part one
with open('./input.txt') as file:
	grid = map(lambda x: x.strip(), file.readlines())

position_virus = [(len(grid)-1)/2, (len(grid[0])-1)/2]
facing = 0
directions = {0:[-1,0], 1:[0,1], 2:[1,0], 3:[0,-1]}
grid = transform_dict(grid)
bursts = 0
infections = 0
while True:
	key_grid = '{:d},{:d}'.format(position_virus[0], position_virus[1])
	if key_grid in grid:
		node = grid[key_grid]
	else:
		grid[key_grid] = '.'
		node = '.'
	if node == '.':
		facing = (facing - 1) % 4
		grid[key_grid] = 'W'
	elif node == 'W':
		infections += 1
		grid[key_grid] = '#'
	elif node == '#':
		facing = (facing + 1) % 4
		grid[key_grid] = 'F' 
	elif node == 'F':
		grid[key_grid] = '.' 
		facing = (facing - 2) % 4
	position_virus = map(add, position_virus, directions[facing])
	bursts += 1
	if bursts % 1000000 == 0:
		print 'Computed {:d} bursts out of 10000000'.format(bursts)
	if bursts == 10000000:
		break
print 'Part two: the number of infections is {:d}'.format(infections)