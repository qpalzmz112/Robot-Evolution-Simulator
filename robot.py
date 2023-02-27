import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import pybullet as p
from sensor import SENSOR
from motor import MOTOR
import os
import math

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")
        self.robotId = p.loadURDF("body" + str(solutionID) + ".urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        os.system("del brain" + solutionID + ".nndf")
        os.system("del body" + solutionID + ".urdf")

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for s in self.sensors:
            self.sensors[s].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronName in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronName):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
                desiredAngle = self.nn.Get_Value_Of(neuronName)
                self.motors[jointName].Set_Value(self, desiredAngle)

    def Think(self):
        if len(self.sensors.keys()):
            self.nn.Update()

    def Get_Fitness(self):
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        basePosition = basePositionAndOrientation[0]
        distance = (basePosition[0]**2+basePosition[1]**2)**.5
        f = open("tmp" + str(self.solutionID) + ".txt", "w")
        f.write(str(distance))
        f.close()
        #os.chmod("tmp" + str(self.solutionID) + ".txt", 0o777)
        os.rename("tmp"+str(self.solutionID)+".txt" , "fitness"+str(self.solutionID)+".txt")