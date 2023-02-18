from ast import Str
from operator import length_hint
import pyrosim.pyrosim as pyrosim
import random
import numpy
import os
import time
import constants as c
from genotype import GENOTYPE

class SOLUTION:
    def __init__(self, ID):
        #self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * c.motorJointRange - (c.motorJointRange/2)
        self.myID = ID
        self.genotype = GENOTYPE()

    def Set_ID(self, ID):
        self.myID = ID
        
    def Start_Simulation(self, directOrGui):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("start /B py simulate.py " + directOrGui + " " + str(self.myID))

    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness" + str(self.myID) + ".txt"):
            time.sleep(0.01)
        f = open("fitness" + str(self.myID) + ".txt", "r")
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
        os.system("del world" + str(self.myID) + ".sdf")

    def Create_World(self):
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.End()

    def Generate_Body(self):
        #pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        # randomly decide number of 'steps': 2-5
        # choose random bound for link dimensions 
        # store link info in tree - first node is root, next nodes are links connected to root, so on
        # for each link, choose number of children: 0-4? and choose direction relative to parent, don't repeat directions
        # while making tree, choose link dimensions and coordinates, choose if link has a sensor
        # create links while making tree, add joints too

        # store joint names in a list
        # send a motor to each joint

        self.genotype.Generate_Body(self.myID)

        #pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        counter = 0
        for linkName in self.genotype.sensorLinks:
            pyrosim.Send_Sensor_Neuron(name = str(counter), linkName = linkName)
            counter += 1

        for jointName in self.genotype.jointNames:
            pyrosim.Send_Motor_Neuron(name = str(counter), jointName = jointName)
            counter += 1
     
        numSensors = len(self.genotype.sensorLinks)
        numMotors = len(self.genotype.jointNames)
        self.weights = numpy.random.rand(numSensors, numMotors) * c.motorJointRange - (c.motorJointRange/2)
        for currentRow in range(numSensors):
            for currentColumn in range(numMotors): #num motor neurons
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn + numSensors, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        return
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow][randomColumn] = random.random() * c.motorJointRange - (c.motorJointRange/2)