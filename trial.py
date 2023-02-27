import os
from parallelHillClimber import PARALLEL_HILLCLIMBER
import random


os.system("del .\data\*.npy")
for i in range(1, 6):
    random.seed(i)
    phc = PARALLEL_HILLCLIMBER()
    phc.Evolve(i)
    #input("Press Enter to continue...")
    #phc.Show_Best()
    #input("Press Enter to continue...")
os.system("start py graph.py")