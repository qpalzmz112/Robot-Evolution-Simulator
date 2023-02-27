from solution import SOLUTION
import constants as c
import copy
import os
import numpy

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        os.system("del fitness*.txt")
        os.system("del brain*.nndf")
        os.system("del world*.sdf")
        os.system("del body*.urdf")
        self.values = numpy.zeros(c.numberOfGenerations)
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Evolve(self, trialNum=-1):
        self.Evaluate(self.parents)
        for i in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(i)
            self.values[i] = self.Best_Fitness()
        if trialNum != -1:
            numpy.save("".join(["data/Trial", str(trialNum), "BestFitness.npy"]), self.values)

    def Evolve_For_One_Generation(self, num):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        print("\n\n\n\n\n")
        print("Generation number: " + str(num))
        print("\n\n\n\n\n")

    def Spawn(self):
        self.children = {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1

    def Mutate(self):
        for key in self.children.keys():
            self.children[key].Mutate()

    def Select(self):
        for k in self.parents.keys():
            if self.parents[k].fitness < self.children[k].fitness:
                self.parents[k] = self.children[k]

    def Evaluate(self, solutions):
        for k in solutions.keys():
            solutions[k].Start_Simulation("DIRECT ")
        for k in solutions.keys():
            solutions[k].Wait_For_Simulation_To_End()

    def Show_Best(self):
        max = self.parents[0].fitness
        ind = 0
        for k in self.parents.keys():
            if self.parents[k].fitness > max:
                max = self.parents[k].fitness
                ind = k
        print("fitness: " + str(max))
        self.parents[ind].Start_Simulation("GUI")

    def Best_Fitness(self):
        max = self.parents[0].fitness
        for k in self.parents.keys():
            if self.parents[k].fitness > max:
                max = self.parents[k].fitness
        return max
    
    def Print(self):
        for k in self.parents.keys():
            print('\n', "parent fitness: ", self.parents[k].fitness, " child fitness: ", self.children[k].fitness, '\n')
