import numpy as np

# class Particle:
#     def __init__(self, pos_x, pos_y, mass, vel_x, vel_y, brightness):
#         self.pos_x = pos_x
#         self.pos_y = pos_y
#         self.mass = mass
#         self.vel_x = vel_x
#         self.vel_y = vel_y
#         self.brightness = brightness


def get_particle_data(particles_data): 
    number_of_particles = round(len(particles_data) / 6)
    particle_arr = np.zeros((number_of_particles, 6), dtype=float)
    #take 6 elements of particles_data at a time and put into each index of particles_arr
    for i in range(len(particle_arr)):
        #particle_arr[i] = Particle(particles_data[0 + i],
        #                            particles_data[1 + i],
        #                            particles_data[2 + i],
        #                            particles_data[3 + i],
        #                            particles_data[4 + i],
        #                            particles_data[5 + i])
        particle_arr[i][0] = particles_data[0 + i] # pos x
        particle_arr[i][1] = particles_data[1 + i] # pos y
        particle_arr[i][2] = particles_data[2 + i] # mass
        particle_arr[i][3] = particles_data[3 + i] # vel x
        particle_arr[i][4] = particles_data[4 + i] # vel y
        particle_arr[i][5] = particles_data[5 + i] # brightness
    return particle_arr



snopp = get_particle_data(np.fromfile("Nbody/input_data/circles_N_4.gal",dtype=float))
print(snopp)