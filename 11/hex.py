import operator

with open('input.txt') as file:
    path = file.read().strip().split(',')

## Position (x, y)
nw, n, ne, sw, s, se = (-0.5, 0.5), (0, 1), (0.5, 0.5), (-0.5, -0.5), (0, -1), (0.5, -0.5)

max_steps = 0
pos = (0, 0)
for step in path:
    pos = tuple(map(operator.add, pos, eval(step)))
    ## As there is no w/e the y term does not matter if |x| > |y| as we need to do 2*|x| steps anyway 
    if abs(pos[0]) > abs(pos[1]):
        steps = 2*abs(pos[0]) 
    else:
        steps = (abs(pos[1]) + abs(pos[0]))
    
    if steps > max_steps:
        max_steps = steps 

print 'Part one: ' + str(steps)

print 'Part two: ' + str(max_steps)