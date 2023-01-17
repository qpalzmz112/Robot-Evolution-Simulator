from struct import pack
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import matplotlib.pylab as plt
import numpy
import time
import random

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)


bAmplitude = numpy.pi/4
bFrequency = 20
bPhaseOffset = 0
bTargetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
for i in range(0, 1000):
    bTargetAngles[i] = bAmplitude*numpy.sin(bFrequency * bTargetAngles[i] + bPhaseOffset)
#numpy.save("data/bTargetAngles.npy", bTargetAngles)

fAmplitude = numpy.pi/4
fFrequency = 10
fPhaseOffset = numpy.pi/4
fTargetAngles = numpy.linspace(0, 2*numpy.pi, 1000)
for i in range(0, 1000):
    fTargetAngles[i] = fAmplitude*numpy.sin(fFrequency * fTargetAngles[i] + fPhaseOffset)
#numpy.save("data/fTargetAngles.npy", fTargetAngles)

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")    

    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b'BackLeg_Torso',controlMode = p.POSITION_CONTROL,targetPosition = bTargetAngles[i],maxForce = 500)
    pyrosim.Set_Motor_For_Joint(bodyIndex = robotId,jointName = b'Torso_FrontLeg',controlMode = p.POSITION_CONTROL,targetPosition = -1*fTargetAngles[i],maxForce = 500)

    time.sleep(1/60)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
p.disconnect()