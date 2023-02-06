import pyrosim.pyrosim as pyrosim
import random
import numpy
import os
import time
import constants as c

class SOLUTION:
    def __init__(self, ID):
        self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
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

        pyrosim.Send_Cube(name="Col1", pos=[-2, -1, 0.75], size=[0.3, 0.3, 1.5], mass=1000)
        pyrosim.Send_Cube(name="Col2", pos=[2, -1, 0.75], size=[0.3, 0.3, 1.5], mass=1000)
        pyrosim.Send_Cube(name="Bar1", pos=[0, -1, 1.6], size=[4, 0.2, 0.2], mass=1000)

        pyrosim.Send_Cube(name="Col3", pos=[-2, 1, 0.75], size=[0.3, 0.3, 1.5], mass=1000)
        pyrosim.Send_Cube(name="Col4", pos=[2, 1, 0.75], size=[0.3, 0.3, 1.5], mass=1000)
        pyrosim.Send_Cube(name="Bar2", pos=[0, 1, 1.6], size=[4, 0.2, 0.2], mass=1000)

        pyrosim.Send_Cube(name="Col5", pos=[-2, 0, 1.25], size=[0.3, 0.3, 2.5], mass=1000)
        pyrosim.Send_Cube(name="Col6", pos=[2, 0, 1.25], size=[0.3, 0.3, 2.5], mass=1000)
        pyrosim.Send_Cube(name="Bar3", pos=[0, 0, 2.6], size=[4, 0.2, 0.2], mass=1000)

        pyrosim.Send_Cube(name="Col7", pos=[-1.6, 0, 0.4], size=[0.3, 0.3, 0.8], mass=1000)
        pyrosim.Send_Cube(name="Col8", pos=[1.6, 0, 0.4], size=[0.3, 0.3, 0.8], mass=1000)
        pyrosim.Send_Cube(name="Bar4", pos=[0, 0, 0.9], size=[3.2, 0.2, 0.2], mass=1000)

        #pyrosim.Send_Cube(name="Col9", pos=[-2, -1.5, 1.25], size=[0.3, 0.3, 2.5], mass=1000)
        #pyrosim.Send_Cube(name="Col10", pos=[2, -1.5, 1.25], size=[0.3, 0.3, 2.5], mass=1000)
        #pyrosim.Send_Cube(name="Bar5", pos=[0, -1.5, 2.6], size=[4, 0.2, 0.2], mass=1000)

        pyrosim.End()

    def Generate_Body(self):
        pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")

        pyrosim.Send_Cube(name="Base", pos=[0, 0, 4], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="Base_L1", parent="Base", child="L1", type = "revolute", position=[0,-0.1,4], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L1", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L1_L2", parent="L1", child="L2", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L2", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L2_L3", parent="L2", child="L3", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L3", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L3_L4", parent="L3", child="L4", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L4", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L4_L5", parent="L4", child="L5", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L5", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L5_L6", parent="L5", child="L6", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L6", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L6_L7", parent="L6", child="L7", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L7", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L7_L8", parent="L7", child="L8", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L8", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="L8_L9", parent="L8", child="L9", type = "revolute", position=[0,-0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="L9", pos=[0, -0.1, 0], size=[0.5,0.2,0.1])

        pyrosim.Send_Joint(name="Base_R1", parent="Base", child="R1", type = "revolute", position=[0, 0.1, 4], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="R1", pos=[0, 0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="R1_R2", parent="R1", child="R2", type = "revolute", position=[0,0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="R2", pos=[0, 0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="R2_R3", parent="R2", child="R3", type = "revolute", position=[0,0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="R3", pos=[0, 0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="R3_R4", parent="R3", child="R4", type = "revolute", position=[0,0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="R4", pos=[0, 0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="R4_R5", parent="R4", child="R5", type = "revolute", position=[0,0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="R5", pos=[0, 0.1, 0], size=[0.5,0.2,0.1])
        pyrosim.Send_Joint(name="R5_R6", parent="R5", child="R6", type = "revolute", position=[0,0.2,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="R6", pos=[0, 0.1, 0], size=[0.5,0.2,0.1])

        pyrosim.End()

    def Generate_Brain(self):
        pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")

        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Base")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "L1")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "L2")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "L3")
        pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "L4")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "L5")
        pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "L6")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "L7")
        pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "L8")
        pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "L9")
        pyrosim.Send_Sensor_Neuron(name = 10, linkName = "R1")
        pyrosim.Send_Sensor_Neuron(name = 11, linkName = "R2")
        pyrosim.Send_Sensor_Neuron(name = 12, linkName = "R3")
        pyrosim.Send_Sensor_Neuron(name = 13, linkName = "R4")
        pyrosim.Send_Sensor_Neuron(name = 14, linkName = "R5")
        pyrosim.Send_Sensor_Neuron(name = 15, linkName = "R6")
        pyrosim.Send_Motor_Neuron(name = 16, jointName = "Base_L1")
        pyrosim.Send_Motor_Neuron(name = 17, jointName = "Base_R1")
        pyrosim.Send_Motor_Neuron(name = 18, jointName = "L1_L2")
        pyrosim.Send_Motor_Neuron(name = 19, jointName = "L2_L3")
        pyrosim.Send_Motor_Neuron(name = 20, jointName = "L3_L4")
        pyrosim.Send_Motor_Neuron(name = 21, jointName = "L4_L5")
        pyrosim.Send_Motor_Neuron(name = 22, jointName = "L5_L6")
        pyrosim.Send_Motor_Neuron(name = 23, jointName = "L6_L7")
        pyrosim.Send_Motor_Neuron(name = 24, jointName = "L7_L8")
        pyrosim.Send_Motor_Neuron(name = 25, jointName = "L8_L9")
        pyrosim.Send_Motor_Neuron(name = 26, jointName = "R1_R2")
        pyrosim.Send_Motor_Neuron(name = 27, jointName = "R2_R3")
        pyrosim.Send_Motor_Neuron(name = 28, jointName = "R3_R4")
        pyrosim.Send_Motor_Neuron(name = 29, jointName = "R4_R5")
        pyrosim.Send_Motor_Neuron(name = 30, jointName = "R5_R6")

        for currentRow in range (c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow, targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])
        pyrosim.End()

    def Mutate(self):
        randomRow = random.randint(0, 2)
        randomColumn = random.randint(0, 1)
        self.weights[randomRow][randomColumn] = random.random() * 2 - 1