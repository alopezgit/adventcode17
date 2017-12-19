def check_where_next(status):
    ### After arriving at a +, this function decides the direction (e.g. left or right)
    ### We only modify the direction
    offset = 0
    pos = status['pos']
    axis = status['axis']
    while True:
        offset += 1
        ind_1 = pos[:]
        ind_2 = pos[:]
        ind_1[axis] = pos[axis]-offset
        ind_2[axis] = pos[axis]+offset
        if ind_1[axis] > 0 and (tubes[ind_1[0]][ind_1[1]] == status['char_axis'][axis] or  tubes[ind_1[0]][ind_1[1]] == '+'):
            status['direction'] = -1
            return status
        elif ind_2[axis] < status['length'][axis] and (tubes[ind_2[0]][ind_2[1]] == status['char_axis'][axis] or  tubes[ind_2[0]][ind_2[1]] == '+'):
            status['direction'] = 1
            return status


def follow_path(status):
    pos = status['pos']
    direction = status['direction']
    axis = status['axis']
    finish = 0
    while not finish:
        pos[status['axis']] += status['direction']
        status['n_steps'] += 1
        next_char = tubes[status['pos'][0]][status['pos'][1]]
        ## Check if it is a letter. If it is, we save it and record steps
        if next_char.istitle():
            status['letters'].append(next_char)
            status['n_steps_letter'] = status['n_steps']
        elif next_char == '+':
            pos_tmp = status['pos'][:]
            pos_tmp[axis] += status['direction']
            ## We check if after the + there is a symbol following the same direction we are going
            ## e.g. ---   +-  This means that we should finish.
            try:
                if status['char_axis'][status['axis']] in tubes[pos_tmp[0]][pos_tmp[1]]:
                    finish = 1
                    break
            except IndexError:
                print 'Out of bounds in {:d}, {:d}'.format(pos_tmp[0], pos_tmp[1])
            ## As we arrive at +, we change the axis and check what direction to follow
            status['axis'] = status['axis'] = (status['axis']+1) % 2
            check_where_next(status)
        ## Check if we go out of bounds    
        if (status['direction'] == -1 and pos[status['axis']]==0) or (status['direction'] == 1 and pos[status['axis']]==status['length'][status['axis']]-1):
            finish = 1
    return status



## Parse getting rid of the newline symbols at the end of each line
with open('input.txt') as file:
    tubes = map(lambda x: x.strip('\n'), file.readlines())

## Build status (pos is x,y, where x (axis=0) is rows and y (axis=1) columns)
status = {'pos':[0,0], 'direction': 1, 'axis': 0, 'n_steps': 1, 'letters': [], 'char_axis': ['|', '-']}
status['length'] = [len(tubes), len(tubes[0])]
status['pos'][1] = tubes[0].find('|')

status = follow_path(status)

        
            
print "Part one: the letters seen are {:s}".format(''.join(status['letters']))
print "Part two: the number of steps are {:d}".format(status['n_steps_letter'])