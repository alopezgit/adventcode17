def knot_single(circular, length, position = 0, skip = 0):
	for element in length:
		partial = []
		positions = []
		for i in range(element):
			position_element = (position + i) % len(circular)
			partial.append(circular[position_element])
			positions.append(position_element)
		partial = list(reversed(partial))
		for i, position_element in enumerate(positions):
			circular[position_element] = partial[i]
		position += skip + element
		skip += 1
	return circular, position, skip 


with open('input.txt') as file:
	length = map(int, file.read().strip().split(','))

circular = range(256)


circular, position, skip = knot_single(circular, length)

print 'Part one: ' + str(circular[0]*circular[1])

## Part two

with open('input.txt') as file:
	length = file.read().strip()

new_length = []
for element in length:
	new_length.append(ord(element))

new_length += [17, 31, 73, 47, 23]
circular = range(256)

position = 0
skip = 0
for n_round in range(64):
	circular, position, skip = knot_single(circular, new_length, position, skip)

dense_hash = []
for i in range(16):
	partial = circular[i*16:(i+1)*16]
	dense_hash.append(format(reduce(lambda i, j: int(i) ^ int(j), partial), 'x'))
print 'Part two: ' + ''.join(dense_hash)