def check_connections(pipes, connections, program_list):
    ## Recursive function, checks all connections to a query program
    new_connections = []
    for connection in connections:
        if connection not in program_list:
            program_list.append(connection)
            new_connections.append(connection)
    for connection in new_connections:
        program_list = check_connections(pipes, pipes[connection][1], program_list)
    return program_list


with open('input.txt', 'r') as file:
    pipes = map(lambda x: x.strip().split(' <-> '), file.readlines())


## We create a list of [program, connections], mapping all strings to int
pipes = [[int(x[0])] + [map(int, x[1].split(','))] for x in pipes]


programs_found = []
n_groups = 0
for program, connections in pipes:
    if program not in programs_found:
        program_list = []
        program_list.append(int(program))
        program_list = check_connections(pipes, pipes[program][1], program_list)
        if program == 0:
            print 'Part one: the number of programs connected to 0 is {:d}'.format(len(program_list))
        programs_found += program_list
        n_groups += 1
        

print 'Part two: the number of different groups is {:d}'.format(n_groups)