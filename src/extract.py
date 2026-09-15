import numpy as np

def get_particle_data(particles_data): 
    number_of_particles = round(len(particles_data) / 6)
    particle_arr = np.zeros((number_of_particles, 6), dtype=float)
    for i in range(number_of_particles):
        start = 6 * i
        particle_arr[i] = particles_data[start:start + 6]
    return particle_arr

data = get_particle_data(np.fromfile("Nbody/input_data/circles_N_4.gal",dtype=float))
print(data)

print(np.fromfile("Nbody/input_data/circles_N_4.gal",dtype=float))

data.tofile("out.gal")

print(get_particle_data(np.fromfile("out.gal", dtype=float)))