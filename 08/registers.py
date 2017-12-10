import operator

with open('input.txt') as file:
    registers = file.readlines()

max_val = 0
dict_registers = {}
for line in registers:
    register, instruction, value, _, register_cond, operator_file, value_cond  = line.split(' ')
    if register not in dict_registers:
        dict_registers[register] = 0
    if register_cond not in dict_registers: 
        dict_registers[register_cond] = 0     

    if eval(str(dict_registers[register_cond])+ ' ' + operator_file + ' ' +value_cond):
        if 'inc' in instruction: 
            dict_registers[register] += int(value)
        else:
            dict_registers[register] -= int(value)
        sorted_x = sorted(dict_registers.items(), key=operator.itemgetter(1), reverse=True)
        if sorted_x[0][1] > max_val:
            max_val = sorted_x[0][1]
    
sorted_x = sorted(dict_registers.items(), key=operator.itemgetter(1), reverse=True)
print sorted_x[0], max_val