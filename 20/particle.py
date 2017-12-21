from operator import add
def parse_particles(particles):
    ## Form a list of dictionaries with position, velocity and acceleration
    particles_list = []
    for particle in particles:
        dict_particles = {}
        dict_particles['p'] = [int(x) for x in particle.split('<')[1].split('>')[0].split(',')]
        dict_particles['v'] = [int(x) for x in particle.split('<')[2].split('>')[0].split(',')]
        dict_particles['a'] = [int(x) for x in particle.split('<')[3].split('>')[0].split(',')]
        particles_list.append(dict_particles)
    return particles_list

def update_particles(particles):
    ## Update all the particles and compute manhattan distance
    min_dist = 1e15
    for n_particle, particle in enumerate(particles):
        particle['v'] = map(add, particle['a'], particle['v'])
        particle['p'] = map(add, particle['p'], particle['v'])
        particle['manhattan'] = reduce(lambda x,y: abs(x)+abs(y), particle['p'])
        if particle['manhattan'] < min_dist:
            min_dist = particle['manhattan']
            particle_closest = n_particle
    return particles, particle_closest, min_dist

def check_collisions(particles):
    ## Check if there are collisions in that time-step, and pop from list the colliding particles
    position_check = 0
    while True:
        pop_elements = [i for i in range(position_check+1, len(particles)) if particles[i]['p'] == particles[position_check]['p']]
        if len(pop_elements) == 0:
            position_check += 1
        else:
            pop_elements.insert(0, position_check)
            for i in reversed(pop_elements):
                particles.pop(i)
        if position_check == len(particles):
            break
    return particles


for part_number in range(1, 3):
    with open('input.txt') as file:
        particles = parse_particles(file.readlines())
    while True:
        particles, particle_closest, min_dist = update_particles(particles)
        ## If we are doing the second part of the puzzle, check if there are collisions 
        if part_number == 2:
            particles = check_collisions(particles)
        ## Distance is arbitary (has to be big enough)
        if min_dist > 1e6:
            if part_number == 1:
                print 'Part one: closest particle is {:d}'.format(particle_closest)
            elif part_number == 2:
                print 'Part two: number of particles is {:d}'.format(len(particles))
            break

