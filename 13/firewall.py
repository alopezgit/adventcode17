def deepish_copy(org):
    ## Taken from https://writeonly.wordpress.com/2009/05/07/deepcopy-is-a-pig-for-simple-data/
    ## copy.deepcopy was quite slow
    out = dict().fromkeys(org)
    for k,v in org.iteritems():
        try:
            out[k] = v.copy()   # dicts, sets
        except AttributeError:
            try:
                out[k] = v[:]   # lists, tuples, strings, unicode
            except TypeError:
                out[k] = v      # ints
 
    return out

def get_severity(firewalls, dict_pos = {}, find_zero = False):
    severity = 0
    max_range = max(firewalls.keys())
    caught = False
    for i in range(max_range+1):
        if i in dict_pos and dict_pos[i]['pos'] == 0:
            severity += firewalls[i] * i
            caught = True        
        dict_pos = increment_position(firewalls, dict_pos)
        if find_zero and caught:
            break
    return severity, caught

def increment_position(firewalls, dict_pos):
    for element in firewalls:
        if element not in dict_pos:
            dict_pos[element] = {}
            dict_pos[element]['pos'] = 0
            dict_pos[element]['traj'] = 1
        if firewalls[element] == 0:
            continue
        if dict_pos[element]['traj'] == 1:
            dict_pos[element]['pos'] = (dict_pos[element]['pos']+1)
        else:
            dict_pos[element]['pos'] = (dict_pos[element]['pos']-1)
        if dict_pos[element]['pos'] == firewalls[element] - 1 or dict_pos[element]['pos']==0:
            dict_pos[element]['traj'] *= -1
    return dict_pos

with open('input.txt') as file:
    firewalls = dict((map(lambda x: map(int, x.strip().split(': ')), file.readlines())))

print 'Part one: severity is {:d}'.format(get_severity(firewalls)[0])

dict_pos = {}

## Initial delay
delay = 2000000
## Initial position
if delay > 0:
    for i in range(delay):
        dict_pos = increment_position(firewalls, dict_pos)
        print i

while True:
    severity, caught = get_severity(firewalls, deepish_copy(dict_pos), find_zero = True)
    if caught:
        delay +=1
    else:
        break
    dict_pos = increment_position(firewalls, dict_pos)
    print delay
print 'Part two: the minimum delay is {:d} picoseconds'.format(delay)