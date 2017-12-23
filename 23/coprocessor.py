#########################################################
######## FUNCTIONS FROM DAY 18 ##########################
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
    n_mul = 0
    n_instructions = 0
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
            n_mul += 1
        elif instruction == 'sub':
            registers[register] -= value
        elif instruction == 'jnz':
            ## Check if register is directly an int, or if it points to a register
            if (not check_int(register) and registers[register] != 0) or (check_int(register) and register != 0):
                program['n_instruction'] += int(value) - 1
        program['n_instruction'] += 1
        ## In case we reach the end, finish
        n_instructions += 1
        if program['n_instruction'] == len(program['instructions']):
            return n_mul


#########################################################
######## BEGIN MAIN CODE ################################
#########################################################

### Part one

with open('input.txt') as file:
    instructions = map(lambda x: x.strip().split(' '), file.readlines())


program = {'n_instruction':0, 'waiting':0, 'registers': {}, 'receive':[], 'instructions':instructions}

n_mul = run_instructions(program, part_two = 0)

print 'Part one: the number of multiplications is {:d}'.format(n_mul)

### Part two
## We optimize the input program by inspecting the input.txt file
## The code with a = 1 checks the number of non-prime numbers between b and c in jumps of 17
## (b-c)/17 - h is the number of prime numbers among the numbers checked, 95 in this case

## If a == 0, the code checks if b is prime (h==0 is prime, h==1 not prime)

## Initialize registers
h = 0
a = 1
b = 67
c = b
if a != 0:
    b = b*100 + 100000 # 106700
    c = b + 17000 # 123000

## The loop with a = 1 runs from b=[106700 to 123000]
initial = b
for b in range(initial, c+1, 17):
    ## After b*0.5, no dividend will be found
    ## The d+=1 is not a good choice, it is slow. 
    ## Could be optimized by increasing faster d as d gets closer to b
    for d in range(2,int(b*0.5)):
        if b % d == 0:
            h += 1
            break
        
       
print 'Part two: the value of the h register is {:d}'.format(h)