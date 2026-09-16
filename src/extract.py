import numpy as np
import subprocess

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

N, snopp = get_particle_data(np.fromfile(inputFile, dtype=float))

for i in range(N):
    #take some steps
    snopp = snopp

print(snopp)

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