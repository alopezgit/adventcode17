#########################################################
######## DEFINE FUNCTIONS ###############################
#########################################################

## Check if string is an integer
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def run_instructions(program, part_two = 0):
    #### The function in part one returns a value, which is the first recovered sound
    #### In part two returns a value (int or register), if sending or receiving (0/1) and the programs dictionary

    ## Take registers from program dictionary
    registers = program['registers']
    while True:
        ## Read instruction
        argument = program['instructions'][program['n_instruction']]
        instruction = argument[0]
        register = argument[1]
        ## If we have three arguments we check if it is a register or int
        if len(argument) == 3:
            value = argument[2]
            if check_int(value):
                value = int(value)
            else:
                value = registers[value]
        ## Initialize registers if it not a number        
        if not check_int(register) and register not in registers:
            registers[register] = 0
        if instruction == 'set':
            registers[register] = value
        elif instruction == 'mul':
            registers[register] *= value
        elif instruction == 'add':
            registers[register] += value
        elif instruction == 'mod':
            registers[register] = registers[register] % value
        elif instruction == 'snd':
            ## Check if we send register's value or number
            ## Behaviour depends on part of problem
            if not check_int(register):
                registers['last_played'] = registers[register]
            else:
                registers['last_played'] = int(register)
            if part_two == 1:
                program['n_instruction'] += 1
                return registers['last_played'], 0, program
                break            
        elif instruction == 'rcv':
            ## Behaviour depends on part of problem
            if registers[register] != 0 and part_two == 0:
                recovered = registers['last_played']
                return recovered
            if part_two == 1:
                program['n_instruction'] += 1
                return register, 1, program
        elif instruction == 'jgz':
            ## Check if register is directly an int, or if it points to a register
            if (not check_int(register) and registers[register] > 0) or (check_int(register) and register > 0):
                program['n_instruction'] += int(value) - 1
        program['n_instruction'] += 1
        ## In case we reach the end, finish
        if program['n_instruction'] == len(program['instructions']):
            break

def run_until_lock(program, receive_list):
    ## Run program until it is waiting to receive a value
    while not program['waiting']:
        value, snd_rcv, program = run_instructions(program, 1)
        if snd_rcv == 0:
            program['n_send'] += 1
            receive_list.append(value)
        elif snd_rcv == 1 and len(program['receive']) > 0:
            program['registers'][value] = program['receive'].pop(0)
        else:
            program['waiting'] = 1
            program['waiting_reg'] = value

    return program


#########################################################
######## BEGIN MAIN CODE ################################
#########################################################

### Part one

with open('input.txt') as file:
    instructions = map(lambda x: x.strip().split(' '), file.readlines())


program = {'n_instruction':0, 'waiting':0, 'registers': {}, 'receive':[], 'instructions':instructions}

recovered = run_instructions(program, part_two = 0)

print 'Part one: The first recovered value is {:d}'.format(recovered)

### Part two

n_send = 0
program_0 = {'n_instruction':0, 'waiting':0, 'registers': {'p':0}, 'receive':[], 'instructions':instructions, 'n_send':0}
program_1 = {'n_instruction':0, 'waiting':0, 'registers': {'p':1}, 'receive':[], 'instructions':instructions, 'n_send':0}
while True:

    program_0 = run_until_lock(program_0, program_1['receive'])

    if program_1['waiting'] == 1 and len(program_1['receive']) > 0:
        program_1['waiting'] = 0
        program_1['registers'][program_1['waiting_reg']] = program_1['receive'].pop(0)

    program_1 = run_until_lock(program_1, program_0['receive'])

    if program_0['waiting'] == 1 and len(program_0['receive']) > 0:
        program_0['waiting'] = 0
        program_0['registers'][program_0['waiting_reg']] = program_0['receive'].pop(0)
    
    if program_0['waiting'] == 1 and program_1['waiting'] == 1:
        break
    
print 'Part two: The number of elements sent by program 1 is {:d}'.format(program_1['n_send'])