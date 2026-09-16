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

inputFile = "Nbody/input_data/ellipse_N_00010.gal"
outputFile = "outputs/out.gal"
compareFile = "Nbody/ref_output_data/ellipse_N_00010_after200steps.gal"

N, particles = get_particle_data(np.fromfile(inputFile, dtype=float))
# print("Input:")
# print(snopp)

# N1, comp = get_particle_data(np.fromfile(compareFile, dtype=float))
# print("Compare:")
# print(comp)

#Calc short for calculator
#trut /\

EPSILON = 1e-3
TIMESTEP = 1e-5
G = 100 / N
NUM_STEPS = 200

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
            #sum_vec += (m[j] / math.pow(distance(i, j) + EPSILON, 3)) * distance_vector(i,j)
            sum_vec += (m[j] / (distance(i, j) + EPSILON) ** 3) * distance_vector(i,j)
    return np.multiply(-G * m[i], sum_vec)

def current_acc(i): # calc is short for calulate acc is short for vroooooooom
    return np.divide(The_Force_Luke(i), m[i])

def next_vel(i): # calc is short for calulate vel is short for velocity
    return vel[i] + np.multiply(TIMESTEP, current_acc(i))

def next_pos(i): # calc is short for calulate pos is short for possistion
    return pos[i] + np.multiply(TIMESTEP, next_vel(i))


#Simulate

def step():
    global pos, vel
    next_vel_arr = np.zeros([N, 2])
    next_pos_arr = np.zeros([N, 2])
    for n in range(N):
        next_vel_arr[n] = next_vel(n)
        next_pos_arr[n] = next_pos(n)
    vel = next_vel_arr
    pos = next_pos_arr

def just_run_it_bro():
    for i in range(NUM_STEPS):
        step()


#Animate

import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

    ani = animation.FuncAnimation(fig, update, frames=NUM_STEPS, interval=30, blit=True, repeat=False)
    plt.show()

import time

def just_run_it_bro():
    time_abs_start = time.time()
    for i in range(NUM_STEPS):
        # print("now running step: ", i)
        # time_start = time.time()
        step()
        # time_end = time.time()
        # time_took = time_end-time_start
        # print("step 0 took ", time_took, " seconds")
    time_abs_end = time.time()
    print("total time: ", time_abs_end-time_abs_start)

animate()


out = np.column_stack((pos, m, vel, brightnesses))
#print("Output:")
#print(out)

#Compare output

out.tofile(outputFile)

result = subprocess.run(
    [
        "Nbody/compare_gal_files/compare_gal_files",
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