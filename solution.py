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
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * c.motorJointRange - (c.motorJointRange/2)
        self.myID = ID

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
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
        # randomly decide number of 'steps': 2-5
        # choose random bound for link dimensions 
        # store link info in tree - first node is root, next nodes are links connected to root, so on
        # for each link, choose number of children: 0-4? and choose direction relative to parent, don't repeat directions
        # while making tree, choose link dimensions and coordinates, choose if link has a sensor
        # create links while making tree, add joints too

        # store joint names in a list
        # send a motor to each joint

        genotype = GENOTYPE()
            
        
        #if self.sensors[0]:
        #    col = "green"
        #else:
        #    col = "cyan"
        #pyrosim.Send_Cube(name="L0", pos=[0, 0, 1.5], size=[x,y,z], color=col)
        #pyrosim.Send_Joint(name="L0_L1", parent="L0", child="L1", type = "revolute", position=[0,-y/2,1.5], jointAxis = "1 0 0")

        #for i in range(1, self.chainlen):
        #    x = random.uniform(0.1, bound)
        #    y = random.uniform(0.1, bound)
        #    z = random.uniform(0.1, bound)
        #    if self.sensors[i]:
        #        col = "green"
        #    else:
        #        col = "cyan"
        #    pyrosim.Send_Cube(name='L'+str(i), pos=[0,-y/2,0], size=[x,y,z], color=col)
        #    if i < self.chainlen-1:
        #        pyrosim.Send_Joint(name='L'+str(i)+'_'+'L'+str(i+1),parent='L'+str(i),child='L'+str(i+1),type="revolute",position=[0,-y,0],jointAxis="1 0 0")

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
        pyrosim.End()
        return   
        counter = 0
        for i in range(self.chainlen):
            if self.sensors[i]:
                pyrosim.Send_Sensor_Neuron(name = str(counter), linkName = 'L'+str(i))
                counter += 1
        numSensors = counter
        for i in range(self.chainlen-1):
            pyrosim.Send_Motor_Neuron(name = str(counter), jointName = 'L'+str(i)+'_'+'L'+str(i+1))
            counter += 1
     

        for currentRow in range(numSensors):
            for currentColumn in range(self.chainlen-1): #num motor neurons
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn + numSensors, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow][randomColumn] = random.random() * c.motorJointRange - (c.motorJointRange/2)