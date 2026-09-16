import numpy as np
import extract as ext
EPSILON = 10e-3
TIMESTEP = 10e-5
G = 100 / ext.N

particles = ext.snopp
e_x = np.array([1,0])
e_y = np.array([0,1])

pos = np.column_stack((ext.get_particle_attribute(particles, ext.POS_X), 
                             ext.get_particle_attribute(particles, ext.POS_Y)))
m = ext.get_particle_attribute(particles, ext.MASS)
vel = np.column_stack((ext.get_particle_attribute(particles, ext.VEL_X), 
                             ext.get_particle_attribute(particles, ext.VEL_Y)))
brightnesses = ext.get_particle_attribute(particles, ext.BRIGHTNESS)

def distance(i, j): # smala r
    return np.linalg.norm(distance_vector(i,j))    

def distance_vector(i, j): # tjocka r
    return pos[i] - pos[j]

def The_Force_Luke(i): #THE KRAAAAAAFT
    sum_vec = np.zeros(2)
    for j in range(ext.N):
        if j != i:
            sum_vec += (m[j] / np.pow(distance(i, j) + EPSILON, 3)) * distance_vector(i,j)
    return -G*m[i] * sum_vec

def current_acc(i): # calc is short for calulate acc is short for vroooooooom
    return The_Force_Luke(i) / m[i]

def next_vel(i): # calc is short for calulate vel is short for velocity
    return vel[i] + TIMESTEP * current_acc(i)

def next_pos(i): # calc is short for calulate pos is short for possistion
    return pos[i] + TIMESTEP * next_vel(i)