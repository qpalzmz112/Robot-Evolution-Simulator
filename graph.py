import numpy
import matplotlib.pyplot

for i in range(1, 6):
    x = numpy.load("data/Trial"+str(i)+"BestFitness.npy")
    matplotlib.pyplot.plot(x, label="Seed "+str(i))

matplotlib.pyplot.legend()
matplotlib.pyplot.xlabel("Generation")
matplotlib.pyplot.ylabel("Fitness")
matplotlib.pyplot.show()