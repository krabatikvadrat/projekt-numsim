import numpy as np

POS_X = 0
POS_Y = 1
MASS = 2
VEL_X = 3
VEL_Y = 4
BRIGHTNESS = 5

def get_particle_data(particles_data): 
    number_of_particles = round(len(particles_data) / 6)
    particle_arr = np.zeros((number_of_particles, 6), dtype=float)
    #take 6 elements of particles_data at a time and put into each index of particles_arr
    for i in range(len(particle_arr)):
        start = 6 * i
        particle_arr[i] = particles_data[start: start + 6]
    return particle_arr

def get_particle_attribute(particles, attribute):
    retrieved_attribute = np.zeros(len(particles))
    for i in range(len(particles)):
        retrieved_attribute[i] = particles[i][attribute]
    return retrieved_attribute


snopp = get_particle_data(np.fromfile("Nbody/input_data/circles_N_4.gal",dtype=float))
#snopp = get_particle_data(np.fromfile("outputs/out.data",dtype=float))

print(snopp)
# pos_x = get_particle_attribute(snopp, POS_X)

# print(pos_x)

output = snopp.tofile("outputs/out.data")
