import numpy
import matplotlib.pyplot

#backLegSensorValues = numpy.load("data/backLegSensorValues.npy")
#frontLegSensorValues = numpy.load("data/frontLegSensorValues.npy")
#matplotlib.pyplot.plot(backLegSensorValues, label="backLeg")
#matplotlib.pyplot.plot(frontLegSensorValues, label="frontLeg")
#matplotlib.pyplot.legend()
#matplotlib.pyplot.show()

bTargetAngles = numpy.load("data/bTargetAngles.npy")
matplotlib.pyplot.plot(bTargetAngles, label="bTargetAngle")
fTargetAngles = numpy.load("data/fTargetAngles.npy")
matplotlib.pyplot.plot(fTargetAngles, label="fTargetAngle")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()