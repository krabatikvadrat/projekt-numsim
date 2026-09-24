import numpy as np
import subprocess
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FFMpegWriter

#PART 0: Parameters of the simulation

#Path to file to use as initial conditions
inputFile = "Nbody/input_data/ellipse_N_00010.gal"
#Name of the file to create containing the final set of vales
outputFile = "outputs/out.gal"
#Path to the file used to compare the output file with
compareFile = "Nbody/ref_output_data/ellipse_N_00010_after200steps.gal"

# If 0 just runs it
# If 1 saves the animation as a mp4
# IF 2 shows the animation
What_to_do = 2

# If the compare script shuld be run
compare_output = True

#The total number of steps to take
NUM_STEPS = 200
# The time step in seconds
TIMESTEP = 1e-5


#PART 1: Extracting the file

#When extracting the input file, the below attributes are used to parse the corresponding column
POS_X = 0
POS_Y = 1
MASS = 2
VEL_X = 3
VEL_Y = 4
BRIGHTNESS = 5

#Given a raw input array of N * 6 elements, returns the number of particles (N) and places each particles data into its own column in particle_arr
def get_particle_data(particles_data): 
    number_of_particles = round(len(particles_data) / 6)
    particle_arr = np.zeros((number_of_particles, 6), dtype=float)

    #Take 6 elements of particles_data at a time and put into each index of particles_arr
    for i in range(len(particle_arr)):
        start = 6 * i
        particle_arr[i] = particles_data[start: start + 6]
    return number_of_particles, particle_arr

#Given an array of particle data and an index between 0 and 5, returnes the attribute associated with said index
def get_particle_attribute(particles, attribute):
    retrieved_attribute = np.zeros(len(particles))
    for i in range(len(particles)):
        retrieved_attribute[i] = particles[i][attribute]
    return retrieved_attribute

N, particles = get_particle_data(np.fromfile(inputFile, dtype=float))


#PART 2: Constants, initial values and equations used for the calculation

#A constant used to cap the max force between two particles, keeping the simulation smooth
EPSILON = 1e-3
#Gravity scales inversely with the number of bodies
G = 100 / N

#2D array of initial positions
pos = np.column_stack((get_particle_attribute(particles, POS_X), 
                            get_particle_attribute(particles, POS_Y)))
#1D array of masses
m = get_particle_attribute(particles, MASS)
#2D array of initial velocities
vel = np.column_stack((get_particle_attribute(particles, VEL_X), 
                            get_particle_attribute(particles, VEL_Y)))
#1D array of brightnesses
brightnesses = get_particle_attribute(particles, BRIGHTNESS)

def distance(i, j): # Absolute distance from particle i to j
    return np.linalg.norm(distance_vector(i,j))    

def distance_vector(i, j): # Distance vector from between particle i and j
    return pos[i] - pos[j]

def The_Force_Luke(i): # The force from all other particles onto i
    sum_vec = np.zeros(2)
    for j in range(N):
        if j != i:
            sum_vec += (m[j] / (distance(i, j) + EPSILON) ** 3) * distance_vector(i,j)
    return np.multiply(-G * m[i], sum_vec)

def current_acc(i): # The acceleration of particle i at the current time
    return np.divide(The_Force_Luke(i), m[i])

def next_vel(i): # The velocity of particle i after one time step
    return vel[i] + np.multiply(TIMESTEP, current_acc(i))

def next_pos(i): # The position of particle i after one time step
    return pos[i] + np.multiply(TIMESTEP, next_vel(i))


#PART 3: Simulation

def step(): #The global positions and velocities arrays are updated after one time step
    global pos, vel
    next_vel_arr = np.zeros([N, 2])
    next_pos_arr = np.zeros([N, 2])
    for n in range(N):
        next_vel_arr[n] = next_vel(n)
        next_pos_arr[n] = next_pos(n)
    vel = next_vel_arr
    pos = next_pos_arr

#Animates the movement of the particles
def animate():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_facecolor('black')
    scat = ax.scatter(pos[:, 0], pos[:, 1], s=brightnesses * 5, c='white')
    ax.set_xlim(pos[:,0].min() - 0.5, pos[:,0].max() + 0.5)
    ax.set_ylim(pos[:,1].min() - 0.5, pos[:,1].max() + 0.5)
    ax.set_aspect('equal')

    def update(frame):
        step()
        scat.set_offsets(pos)
        return scat,

    def init():
        scat.set_offsets(pos)
        return scat,

    ani = animation.FuncAnimation(
        fig,
        update,
        init_func=init,
        frames=range(NUM_STEPS),
        interval=30,
        blit=True,
        repeat=False,
    )

    if What_to_do == 1:
        writer = FFMpegWriter(fps=60, bitrate=1800)
        ani.save("outputs/nbody.mp4", writer=writer)

    elif What_to_do == 2:
        plt.show()

#Only runs the simulation
def just_run_it():
    time_abs_start = time.time()
    for i in range(NUM_STEPS):
        step()
    time_abs_end = time.time()
    print("total time: ", time_abs_end-time_abs_start)

if What_to_do == 0:
    just_run_it()
else:
    animate()


#PART 4: evaluating the results

compare_gal_files_path = "Nbody/compare_gal_files/compare_gal_files"

#Runs the provided C program for comparing outputs (compare_gal_files). 
#Note that the program needs to be compiled to the compare_gal_files_path.
if compare_output:
    #"Reassemble" the values into the same format as the input file
    out = np.column_stack((pos, m, vel, brightnesses))

    out.tofile(outputFile)

    #Running the subprocess of comparing
    result = subprocess.run(
        [
            compare_gal_files_path,
            str(N),
            compareFile,
            outputFile
        ],
        capture_output=True,
        text=True
    )

    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    print("return code:", result.returncode)