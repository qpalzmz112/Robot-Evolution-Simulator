import os
from parallelHillClimber import PARALLEL_HILLCLIMBER

os.system("del .\data\*.npy")
phc = PARALLEL_HILLCLIMBER()
phc.Evolve()
phc.Show_Best()

