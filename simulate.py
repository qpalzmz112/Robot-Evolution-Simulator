#from struct import pack
#import pybullet as p
#import pybullet_data
#import pyrosim.pyrosim as pyrosim
#import matplotlib.pylab as plt
#import numpy
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]


simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()