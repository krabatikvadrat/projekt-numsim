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

def acc(i):
    return The_Force_Luke(i) / m[i]

# n is the time t change name later 
def calc_vel_x(): # calc_is_short_for_calculator_vel_is_short_for_velosity_x
    x_vel[i, n+1] = x_vel[i] + TIMESTEP*acc_x(i)

def calc_vel_y(): # calc_is_short_for_calculator_vel_is_short_for_velosity_y
    y_vel[i, n+1] = y_vel[i] + TIMESTEP*acc_y(i)

def calc_pos_x(): # calc_is_short_for_calculator_vel_is_short_for_possistion_x
    x_pos[i, n+1] = x_pos[i] + TIMESTEP*vel_x[i, n+1]

def calc_pos_y(): # calc_is_short_for_calculator_vel_is_short_for_possistion_y
    y_pos[i, n+1] = x_pos[i] + TIMESTEP*vel_y[i, n+1]