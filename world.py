import pybullet as p
import time
import os

class WORLD:
    def __init__(self, ID):
        self.planeId = p.loadURDF("plane.urdf")
        while not os.path.exists("world" + str(ID) + ".sdf"):
            time.sleep(0.01)
        self.objects = p.loadSDF("world" + str(ID) + ".sdf") 
