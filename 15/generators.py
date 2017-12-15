
def get_match(value_A, value_B):
    bits_A = bin(value_A)[2:].zfill(32)[-16:]
    bits_B = bin(value_B)[2:].zfill(32)[-16:]
    return bits_B == bits_A

def next_remainder(gen):
    divide_by = 2147483647
    gen['last'] = (gen['last']*gen['factor'])%divide_by
    return gen

def init_generators():
    gen_A = {}
    gen_B = {}
    gen_A['factor'] = 16807
    gen_A['last'] = 277
    gen_B['factor'] = 48271
    gen_B['last'] = 349
    return gen_A, gen_B


## Part one

gen_A, gen_B = init_generators()
n_match = 0
for i in range(int(4e7)):
    gen_A = next_remainder(gen_A)
    gen_B = next_remainder(gen_B)
    n_match += get_match(gen_A['last'], gen_B['last'])
    if i % 10000 == 0:
        print '{:d} pairs computed out of {:d}'.format(i, int(4e7))

matches_part_1 = n_match
print '\nPart one: Number of matches is {:d}\n'.format(matches_part_1)



## Part two
import time
print '####### Starting Part Two #######'
time.sleep(3)

gen_A, gen_B = init_generators()
A_value, B_value = -1, -1
n_pairs, n_match = 0, 0
while True:
    if A_value == -1:
        gen_A = next_remainder(gen_A)
        if gen_A['last'] % 4 == 0:
            A_value = gen_A['last']

    if B_value == -1:
        gen_B = next_remainder(gen_B)
        if gen_B['last'] % 8 == 0:
            B_value = gen_B['last']

    if A_value >= 0 and B_value >= 0:
        n_pairs += 1
        n_match += get_match(A_value, B_value)
        A_value, B_value = -1, -1

    if n_pairs % 10000 == 0:
        print '{:d} pairs computed out of {:d}'.format(n_pairs, int(5e6))

    if n_pairs == 5e6:
        break


print 'Part one: Number of matches is {:d}'.format(matches_part_1)
print 'Part two: Number of matches is {:d}'.format(n_match)
