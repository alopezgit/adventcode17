

def recursive_weight(key, dict_tower, level = 0):
    dict_tower[key]['level'] = level
    if dict_tower[key]['sum_weight'] == -1 and ('parents' in dict_tower[key]):
        dict_tower[key]['sum_weight'] = 0
        level += 1
        dict_tower[key]['parents_weight'] = []
        for parent in dict_tower[key]['parents']:
            weight_parent = recursive_weight(parent, dict_tower, level)
            dict_tower[key]['parents_weight'].append(weight_parent)
            dict_tower[key]['sum_weight'] += weight_parent
        if len(set(dict_tower[key]['parents_weight'])) > 1:
            wrong = None
            print 'Error', dict_tower[key]['parents_weight']
            for parent in dict_tower[key]['parents']:
                if dict_tower[key]['parents_weight'].count(dict_tower[parent]['sum_weight'] + dict_tower[parent]['weight']) == 1:
                    wrong = parent  
                else:
                    correct_weight = dict_tower[parent]['sum_weight'] + dict_tower[parent]['weight']
            if wrong:
                print 'Change ' +wrong +' to ' + str(correct_weight - dict_tower[wrong]['sum_weight']) + ' (level '+str(dict_tower[wrong]['level'])+')'

        level -= 1
        return dict_tower[key]['sum_weight'] + dict_tower[key]['weight']
    else:
        if 'parents' in dict_tower:
            print dict_tower[key]['parents'], dict_tower[key]['sum_weight'], level
        if dict_tower[key]['sum_weight'] == -1:
            dict_tower[key]['sum_weight'] = 0
        return dict_tower[key]['weight'] + dict_tower[key]['sum_weight']





with open('input.txt') as file:
    tower = file.readlines()

dict_tower = {}
for element in tower:
    name = element.split(' (')[0]
    if name not in dict_tower:
        dict_tower[name] = {}
        dict_tower[name]['sub'] = []

    dict_tower[name]['weight'] = int(element.split(' (')[1].split(')')[0])
    if len(element.split('->')) > 1:
        parents = element.split('->')[1].strip().strip(' ').split(', ')
        dict_tower[name]['parents'] = parents 
        for parent in parents:
            if parent not in dict_tower:
                dict_tower[parent] = {}
            if 'sub' not in dict_tower:
                dict_tower[parent]['sub'] = [name]
            else:
                dict_tower[parent]['sub'].append(name)

for key, value in dict_tower.iteritems():
    if len(dict_tower[key]['sub']) == 0:
        bottom_tower = key
        break
print 'Bottom is: ' +bottom_tower


## Part two
for key in dict_tower:
    dict_tower[key]['sum_weight'] = -1

recursive_weight(bottom_tower, dict_tower)
