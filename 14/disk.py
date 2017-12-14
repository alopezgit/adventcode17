def get_hash(puzzle_input_i):
    length = []
    for element in puzzle_input_i:
        length.append(ord(element))
    length += [17, 31, 73, 47, 23]
    circular = range(256)
    position = 0
    skip = 0
    for n_round in range(64):
        circular, position, skip = knot_single(circular, length, position, skip)
    dense_hash = []
    for i in range(16):
        partial = circular[i*16:(i+1)*16]
        dense_hash.append(format(reduce(lambda i, j: int(i) ^ int(j), partial), 'x'))

    for i, element in enumerate(dense_hash):
        if len(element) == 1:
            dense_hash[i] = '0'+element
    return dense_hash

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


### The functions above are from day 10

puzzle_input = 'oundnydw'
total_1 = 0
matrix = []
for i in range(128):
    puzzle_input_i = puzzle_input + '-' + str(i)
    dense_hash = get_hash(puzzle_input_i)
     ## equals to hexadecimal
    dense_hash = ''.join(dense_hash)
    num_of_bits = 4
    string_bits = ''.join([bin(int(element, 16))[2:].zfill(4) for element in dense_hash])
    total_1 += (string_bits).count('1')
    matrix.append(list(string_bits))

print 'Part one: total number of 1 is {:d}'.format(total_1)

### Part two

def check_i_j(matrix, region, i, j):
    for shift_x in range(-1,2):
        for shift_y in range(-1,2):
            if abs(shift_x) + abs(shift_y) > 1:
                continue
            if i+shift_x > 127 or i+shift_x < 0:
                continue
            if j+shift_y > 127 or j+shift_y < 0:
                continue
            if matrix[i+shift_x][j+shift_y] == '1':
                matrix[i+shift_x][j+shift_y] = '0'
                matrix = check_i_j(matrix, region, i+shift_x, j+shift_y)
    return matrix


i, j = 0, 0
region = 1

while True:
    if matrix[i][j] == '1':
        matrix = check_i_j(matrix, region, i, j)
        if reduce(lambda x, y: x+y, map(lambda x:sum(map(int, x)), matrix)) == 0:
            break
        region += 1
    else:
        i += 1
        if i == len(matrix[0]):
            i = 0
            j += 1

print 'Part two: total number of connected regions is {:d}'.format(region)


