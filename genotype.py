import pyrosim.pyrosim as pyrosim
import random

class NODE:
    def __init__(self, name, dims, pos, color):
        self.name = name
        self.dims = dims
        self.pos = pos
        self.color = color
        self.children = []

    def Add_Child(self, node):
        self.children.append(node)

    def Send_Link(self, color):
        pyrosim.Send_Cube(name=self.name, pos=self.pos, size=self.dims, color=color)

class GENOTYPE:
    def __init__(self):
        depth = random.randint(2, 5)
        bound = random.uniform(0.5, 2)

        root = NODE(name='root', dims=randomDims(bound), pos=[0,0,1], color=randomColor())
        root.Send_Link(root.color)

        numChildren = random.randint(1,4)
        usedDirections = [] # 9 directions: 0 = +z, 1 = +x, 2 = -x, 3 = +y, 4 = -y, 5 = +x+z, 6 = -x+z, 7 = +y+z, 8 = -y+z
        for i in range(numChildren):
            dir = random.randint(0, 8)
            while dir in usedDirections:
                dir = random.randint(0, 8)
            usedDirections.append(dir)

            size=randomDims(bound)
            jointPos = absJointPosFromDir(root.pos, root.dims, dir)
            position = childPosFromDir(size,dir)

            child = NODE(name='A'+str(i), dims=size, pos=position, color=randomColor())
            root.Add_Child(child)

            pyrosim.Send_Joint(name=root.name+'_'+child.name+str(i), parent=root.name, child=child.name, type = "revolute", position = jointPos, jointAxis=randomAxis())
            child.Send_Link(child.color)



def absJointPosFromDir(rootPos, rootDims, dir): # absolute; only use for joints whose parent is root link
    match dir:
        case 0: res=[rootPos[0],rootPos[1],rootPos[2]+rootDims[2]/2]
        case 1: res=[rootPos[0]+rootDims[0]/2,rootPos[1],rootPos[2]]
        case 2: res=[rootPos[0]-rootDims[0]/2,rootPos[1],rootPos[2]]
        case 3: res=[rootPos[0],rootPos[1]+rootDims[1]/2,rootPos[2]]
        case 4: res=[rootPos[0],rootPos[1]-rootDims[1]/2,rootPos[2]]
        case 5: res=[rootPos[0]+rootDims[0]/2,rootPos[1],rootPos[2]+rootDims[2]/2]
        case 6: res=[rootPos[0]-rootDims[0]/2,rootPos[1],rootPos[2]+rootDims[2]/2]
        case 7: res=[rootPos[0],rootPos[1]+rootDims[1]/2,rootPos[2]+rootDims[2]/2]
        case 8: res=[rootPos[0],rootPos[1]-rootDims[1]/2,rootPos[2]+rootDims[2]/2]
    return res

def relJointPosFromDir(jointPos, childDims, dir): # relative to parent joint
    pass

def childPosFromDir(dims, dir): # relative to parent joint
    x=dims[0]
    y=dims[1]
    z=dims[2]
    match dir:
        case 0:
            pos=[0,0,z/2]
        case 1:
            pos=[x/2,0,0]
        case 2:
            pos=[-x/2,0,0]
        case 3:
            pos=[0,y/2,0]
        case 4:
            pos=[0,-y/2,0]
        case 5:
            pos=[x/2,0,z/2]
        case 6:
            pos=[-x/2,0,z/2]
        case 7: 
            pos=[0,y/2,z/2]
        case 8: 
            pos=[0,-y/2,z/2]
    return pos

def randomDims(bound):
    return [random.uniform(0.1, bound), random.uniform(0.1, bound), random.uniform(0.1, bound)]

def randomColor():
    if random.randint(0,1):
        return "green"
    return "cyan"

def randomAxis():
    ax = random.randint(0, 2)
    match ax:
        case 0: axis="1 0 0"
        case 1: axis="0 1 0"
        case 2: axis="0 0 1"
    return axis