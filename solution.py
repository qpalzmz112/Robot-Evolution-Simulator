from ast import Str
from operator import length_hint
from unittest import makeSuite
import pyrosim.pyrosim as pyrosim
import random
import numpy
import os
import time
import constants as c
from genotype import GENOTYPE

class SOLUTION:
    def __init__(self, ID):
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
        while True:
            try:
                f = open("fitness"+str(self.myID)+".txt", "r")
                break
            except:
                pass
        self.fitness = float(f.read())
        f.close()
        os.system("del fitness" + str(self.myID) + ".txt")
        os.system("del world" + str(self.myID) + ".sdf")

    def Create_World(self):
        pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
        pyrosim.Send_Cube(name = "origin", pos = [0, 0, 0.01], size = [0.25, 0.25, 0.02], mass = 10000, color = "cyan")
        pyrosim.End()

    def Generate_Body(self):
        self.genotype.Generate_Body(self.myID)

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
            for currentColumn in range(numMotors):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn + numSensors, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        mutationType = random.randint(1, 2)
        match mutationType:
            case 1: 
                if len(self.genotype.sensorLinks) == 0:
                    return
                
                randomRow = random.randint(0, len(self.genotype.sensorLinks) - 1)
                randomColumn = random.randint(0, len(self.genotype.jointNames) - 1)

                self.weights[randomRow][randomColumn] = random.random() * c.motorJointRange - (c.motorJointRange/2)
                return
            case 2:
                self.genotype.Add_Random_Link()
                return
            #case 3:
             #   self.genotype.Remove_Random_Link()
             #   return
        