from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILLCLIMBER:
    def __init__(self):
        os.system("del fitness*.txt")
        os.system("del brain*.nndf")
        self.nextAvailableID = 0
        self.parents = {}
        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        

    def Evolve(self):
        self.Evaluate(self.parents)
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()

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
            if self.parents[k].fitness > self.children[k].fitness:
                self.parents[k] = self.children[k]

    def Evaluate(self, solutions):
        for k in solutions.keys():
            solutions[k].Start_Simulation("DIRECT ")
        for k in solutions.keys():
            solutions[k].Wait_For_Simulation_To_End()

    def Show_Best(self):
        min = self.parents[0].fitness
        ind = 0
        for k in self.parents.keys():
            if self.parents[k].fitness < min:
                min = self.parents[k].fitness
                ind = k
        self.parents[ind].Start_Simulation("GUI")
    
    def Print(self):
        for k in self.parents.keys():
            print('\n', "parent fitness: ", self.parents[k].fitness, " child fitness: ", self.children[k].fitness, '\n')
