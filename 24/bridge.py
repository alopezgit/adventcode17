## Recursive function, it is slow
def next_port(ports, connection, index_used, strength = 0, length = 0):
	max_strength = 0
	max_strength_length = 0
	max_length = len(index_used)
	for i in range(len(ports)):
		if i in index_used:
			continue
		port = ports[i]
		if connection in port:
			new_connection = port[(port.index(connection) + 1) % 2]
			index_used.append(i)
			strength_tmp, length_tuple = next_port(ports, new_connection, index_used, strength, length)
			strength_tmp += new_connection + connection
			index_used.pop()
			if strength_tmp > max_strength:
				max_strength = strength_tmp
			if length_tuple[0] > max_length:
				max_strength_length = length_tuple[1] + new_connection + connection
				max_length = length_tuple[0]
	return max_strength, (max_length, max_strength_length)
		


with open('input.txt') as file:
	ports = map(lambda x: map(int, x.strip('\n').split('/')), file.readlines())


max_strength = 0
max_length = 0
max_strength_length = 0
index_used = []
for i, port in enumerate(ports):
	index_used.append(i)
	if 0 in port:
		connection = port[(port.index(0) + 1) % 2]
		strength, length = next_port(ports, connection, index_used)
		strength+= connection
		if length[0] >= max_length and length[1] > max_strength_length:
			max_strength_length = length[1] + connection
			max_length = length[0]
		if strength > max_strength:
			max_strength = strength
	index_used.pop()
print 'Part one: Strongest bridge has strength {:d}'.format(max_strength)
print 'Part two: Strongest among longest bridge has strength {:d} and length {:d}'.format(max_strength_length, max_length)
