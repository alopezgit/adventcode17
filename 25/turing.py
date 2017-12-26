def parse_state(state_info, info):
	state = state_info[0][-3]
	info[state] = {}
	if 'left' in state_info[3]:
		direction = -1
	else:
		direction = 1
	info[state]['0'] = {'write': state_info[2][-3], 'direction': direction, 'next_state': state_info[4][-3]}

	if 'left' in state_info[7]:
		direction = -1
	else:
		direction = 1
	info[state]['1'] = {'write': state_info[6][-3], 'direction': direction, 'next_state': state_info[8][-3]}
	return info

def create_dict_turing(text):
	info = {}
	info['initial_state'] = text[0].split('state ')[1][0]
	info['checksum_steps'] = int(text[1].split('after ')[1].split('steps')[0])
	for n_line in range(3, len(text)):
		if 'In state' in text[n_line]:
			info = parse_state(text[n_line:n_line+9], info)
	return info

def run_state(state, tape, position, info_states):
	current_value = tape[position]
	instructions = info_states[state][current_value]
	tape[position] = instructions['write']
	position += instructions['direction']
	next_state = instructions['next_state']
	return tape, position, next_state

with open('input.txt') as file:
	info_states = create_dict_turing(file.readlines())

print info_states

tape = {}
state = info_states['initial_state']
position = 0
for i in range(0, info_states['checksum_steps']):
	if position not in tape:
		tape[position] = '0'
	tape, position, state = run_state(state, tape, position, info_states)
	if i % 1000000 == 0:
		print 'Instruction {:d} out of {:d}'.format(i, info_states['checksum_steps'])
print 'Part one: The amount of 1s in the tape is {:d}'.format(reduce(lambda x, value:x + int(value), tape.itervalues(), 0))

print 'Part two: no need to code :)'