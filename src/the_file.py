import numpy as np
import subprocess

#Extract

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
    return number_of_particles, particle_arr

def get_particle_attribute(particles, attribute):
    retrieved_attribute = np.zeros(len(particles))
    for i in range(len(particles)):
        retrieved_attribute[i] = particles[i][attribute]
    return retrieved_attribute

inputFile = "Nbody/input_data/circles_N_2.gal"
outputFile = "outputs/out.gal"

N, snopp = get_particle_data(np.fromfile(inputFile, dtype=float))

#Calc short for calculator
#trut /\

EPSILON = 10e-3
TIMESTEP = 10e-5
G = 100 / N

particles = snopp
e_x = np.array([1,0])
e_y = np.array([0,1])

pos = np.column_stack((get_particle_attribute(particles, POS_X), 
                             get_particle_attribute(particles, POS_Y)))
m = get_particle_attribute(particles, MASS)
vel = np.column_stack((get_particle_attribute(particles, VEL_X), 
                             get_particle_attribute(particles, VEL_Y)))
brightnesses = get_particle_attribute(particles, BRIGHTNESS)

def distance(i, j): # smala r
    return np.linalg.norm(distance_vector(i,j))    

def distance_vector(i, j): # tjocka r
    return pos[i] - pos[j]

def The_Force_Luke(i): #THE KRAAAAAAFT
    sum_vec = np.zeros(2)
    for j in range(N):
        if j != i:
            sum_vec += (m[j] / np.pow(distance(i, j) + EPSILON, 3)) * distance_vector(i,j)
    return np.multiply(-G * m[i], sum_vec)

def current_acc(i): # calc is short for calulate acc is short for vroooooooom
    return np.divide(The_Force_Luke(i), m[i])

def next_vel(i): # calc is short for calulate vel is short for velocity
    return vel[i] + np.multiply(TIMESTEP, current_acc(i))

def next_pos(i): # calc is short for calulate pos is short for possistion
    return pos[i] + np.multiply(TIMESTEP, next_vel(i))


#Simulate
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

solution = solve_ivp



#Compare output

output = snopp.tofile(outputFile)

result = subprocess.run(
    [
        "Nbody/compare_gal_files/compare_gal_files",
        str(N),
        inputFile,
        outputFile
    ],
    capture_output=True,
    text=True
)

print("stdout:", result.stdout)
print("stderr:", result.stderr)
print("return code:", result.returncode)

