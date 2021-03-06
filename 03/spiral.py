input_number = 325489
sum_numbers = 0
n_square = 0
while True:
	sum_numbers = (2*n_square+1)**2
	if sum_numbers >= input_number:
		ini  = (2*(n_square-1)+1)**2
		remain = input_number - ini
		half_side = (sum_numbers - ini)/8
		if remain/half_side % 2 == 1:
			distance_center = n_square + remain%half_side
		else:
			distance_center = n_square + half_side-remain%half_side
		break
	n_square += 1

print 'Part one: the distance to the center of the spiral is ' + str(distance_center)

## Part two
X = Y = 2*n_square+1
x = y = 0
dx = 0
dy = -1
n_element = 0
dict_grid = {}
for i in range(max(X, Y)**2):
    if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
    	if len(dict_grid)== 0:
    		sum_partial = 1
    		dict_grid[str(x)+','+str(y)] = 1
    	else:
	    	sum_partial = 0
	    	for x_1 in range(x-1,x+2):
	    		for y_1 in range(y-1,y+2):
	    			if str(x_1)+','+str(y_1) in dict_grid:
	    				sum_partial += dict_grid[str(x_1)+','+str(y_1)]
    		dict_grid[str(x)+','+str(y)] = sum_partial
    	n_element+= 1
    	if sum_partial > input_number:
        	print  'Part two: position is ('+str(x)+', '+str(y)+'), sum '+str(dict_grid[str(x)+','+str(y)])+',  and it is the '+str(n_element)+' element of the spiral'
        	break
    if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
        dx, dy = -dy, dx
    x, y = x+dx, y+dy
