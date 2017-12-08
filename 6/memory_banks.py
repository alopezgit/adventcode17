
with open('input.txt') as file:
    memory = map(int, file.read().split('\t'))

n_steps = 0
dict_pos = {}
while True:

    blocks = max(memory)
    index = memory.index(blocks)
    memory[index] = 0
    while True:
        index += 1
        if index == len(memory):
            index = 0
        memory[index] += 1
        blocks -= 1
        if blocks == 0:
            break

    n_steps += 1
    print n_steps
    if ''.join(map(str,memory)) in dict_pos:
        break
    dict_pos[''.join(map(str,memory))] = 1

### Part two
with open('input.txt') as file:
    memory = map(int, file.read().split('\t'))

n_steps = 0
dict_pos = {}
while True:
    blocks = max(memory)
    index = memory.index(blocks)
    memory[index] = 0
    while True:
        index += 1
        if index == len(memory):
            index = 0
        memory[index] += 1
        blocks -= 1
        if blocks == 0:
            break

    n_steps += 1
    if ''.join(map(str,memory)) in dict_pos:
        print n_steps - dict_pos[''.join(map(str,memory))]
        break
    dict_pos[''.join(map(str,memory))] = n_steps
