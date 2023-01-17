import pyrosim.pyrosim as pyrosim
import pybullet as p
import numpy
import constants as c

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.bAmplitude
        self.frequency = c.bFrequency
        self.offset = c.bPhaseOffset
        
        print(self.jointName)
        if self.jointName == b'BackLeg_Torso':
            self.frequency *= 0.5

        self.motorValues = numpy.linspace(0, 2*numpy.pi, 1000)
        for i in range(0, 1000):
            self.motorValues[i] = self.amplitude*numpy.sin(self.frequency * self.motorValues[i] + self.offset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot.robotId,jointName = self.jointName,controlMode = p.POSITION_CONTROL,targetPosition = self.motorValues[t],maxForce = 500)

    def Save_Values(self):
        numpy.save("".join(["data/", self.linkName, "MotorValues.npy"]), self.motorValues)
       