import pyrosim.pyrosim as pyrosim
import random

class LINK_NODE:
    def __init__(self, name, dims, pos, color, depth, dir):
        self.name = name
        self.dims = dims
        self.pos = pos
        self.color = color
        self.children = []
        self.depth = depth
        self.dirFromParent = dir

    def Add_Child(self, node):
        self.children.append(node)

    def Send(self):
        pyrosim.Send_Cube(name=self.name, pos=self.pos, size=self.dims, color=self.color)

    def Print(self):
        print("LINK_NODE: name: "+self.name)

class JOINT_NODE:
    def __init__(self, name, parent, child, pos, axis, link):
        self.name = name  
        self.parent = parent
        self.child = child
        self.pos = pos
        self.axis=axis
        self.children = [link]

    def Send(self):
        pyrosim.Send_Joint(name=self.name, parent=self.parent, child=self.child, type="revolute", position=self.pos, jointAxis=self.axis)

    def Print(self):
        print("JOINT_NODE: name: "+self.name+" position: "+str(self.pos))


class GENOTYPE:
    def __init__(self):
        self.sensorLinks = []
        self.jointNames = []
        self.leaves = []
        self.leafParents = []
        
        depth = random.randint(2, 4) # upper bound: 5?
        
        self.bound = random.uniform(0.5, 1) # upper bound: 2?

        self.root = LINK_NODE(name='root', dims=randomDims(self.bound), pos=[0,0,1], color=randomColor(), depth=0, dir=None)
        if self.root.color == "green":
            self.sensorLinks.append('root')
            
        numChildren = random.randint(1,4) # upper bound: 4?
        usedDirections = [] # 9 directions: 0 = +z, 1 = +x, 2 = -x, 3 = +y, 4 = -y, 5 = +x+z, 6 = -x+z, 7 = +y+z, 8 = -y+z
        todo = []
        for i in range(numChildren):
            dir = random.randint(0, 8)
            while dir in usedDirections:
                dir = random.randint(0, 8)
            usedDirections.append(dir)

            size = randomDims(self.bound)
            jointPos = absJointPosFromDir(self.root.pos, self.root.dims, dir)
            linkPos = relLinkPosFromDir(size,dir)
            
            newLink = LINK_NODE(name='A'+str(i), dims=size, pos=linkPos, color=randomColor(), depth=1, dir=dir)
            newJoint = JOINT_NODE(name="root"+'_'+newLink.name, parent="root", child=newLink.name, pos=jointPos, axis=randomAxis(),link=newLink)
            if newLink.color == "green":
                self.sensorLinks.append(newLink.name)
            self.jointNames.append(newJoint.name)
            self.root.Add_Child(newJoint)
            todo.append(newLink)

        self.counter = 0
        while todo:
            currLink = todo.pop(0)
            
            numChildren = random.randint(1, 1) #2?
            usedDirections = []
            for i in range(numChildren):
                dir = random.randint(0,8)
                while dir in usedDirections:
                    dir = random.randint(0,8)
                usedDirections.append(dir)

                size = randomDims(self.bound)
                jointPos = relJointPosFromDir(currLink.dims, currLink.dirFromParent, dir)
                if jointPos == None:
                    continue # don't add a link that would intersect, may want to work on this
                linkPos = relLinkPosFromDir(size, dir)

                newLink = LINK_NODE(name=chr(currLink.depth+65)+str(self.counter), dims=size, pos=linkPos, color=randomColor(), depth=currLink.depth+1, dir=dir)
                self.counter += 1
                newJoint = JOINT_NODE(name=currLink.name+'_'+newLink.name, parent=currLink.name, child=newLink.name, pos=jointPos, axis=randomAxis(),link=newLink)
                if newLink.color == "green":
                    self.sensorLinks.append(newLink.name)
                self.jointNames.append(newJoint.name)
                currLink.Add_Child(newJoint)
                if (newLink.depth < depth):
                    todo.append(newLink)
                else:
                    self.leafParents.append(currLink)
                    self.leaves.append(newLink)

    def Generate_Body(self, id):
        # start with root
        # add child joints to todo
        # send root
        # for each joint in todo, add its child node to todo then send the joint
        # for each child node in joint, add its children and then send it
        pyrosim.Start_URDF("body" + str(id) + ".urdf")

        todo = [self.root]
        while todo:
            curr = todo.pop(0)
            todo += curr.children
            curr.Send()
        
        pyrosim.End()   

    def Add_Random_Link(self):
        if len(self.leaves) == 0:
            return
        i = random.randint(0, len(self.leaves)-1)
        currLink = self.leaves[i]

        size = randomDims(self.bound)
        
        dir = random.randint(0,8)

        jointPos = relJointPosFromDir(currLink.dims, currLink.dirFromParent, dir)
        while jointPos == None:
            dir = random.randint(0,8)
            jointPos = relJointPosFromDir(currLink.dims, currLink.dirFromParent, dir)
        linkPos = relLinkPosFromDir(size, dir)

        newLink = LINK_NODE(name=chr(currLink.depth+65)+str(self.counter), dims=size, pos=linkPos, color=randomColor(), depth=currLink.depth+1, dir=dir)
        self.counter += 1
        newJoint = JOINT_NODE(name=currLink.name+'_'+newLink.name, parent=currLink.name, child=newLink.name, pos=jointPos, axis=randomAxis(),link=newLink)
        if newLink.color == "green":
            self.sensorLinks.append(newLink.name)
        self.jointNames.append(newJoint.name)
        currLink.Add_Child(newJoint)

    def Remove_Random_Link(self):
        if len(self.leafParents) == 0:
            return
        i = random.randint(0, len(self.leafParents)-1)
        if len(self.leafParents[i].children) == 0:
            return
        j = random.randint(0, len(self.leafParents[i].children)-1)
        joint = self.leafParents[i].children.pop(j)

        self.jointNames.remove(joint.name)
        link = joint.children[0]
        if link.color == "green":
            self.sensorLinks.remove(link.name)
 

def absJointPosFromDir(rootPos, rootDims, dir): # absolute; only use for joints whose parent is root link
    px, py, pz = rootPos[0], rootPos[1], rootPos[2]
    dx, dy, dz = rootDims[0]/2, rootDims[1]/2, rootDims[2]/2
    match dir:
        case 0: res=[px,py,pz+dz]
        case 1: res=[px+dx,py,pz]
        case 2: res=[px-dx,py,pz]
        case 3: res=[px,py+dy,pz]
        case 4: res=[px,py-dy,pz]
        case 5: res=[px+dx,py,pz+dz]
        case 6: res=[px-dx,py,pz+dz]
        case 7: res=[px,py+dy,pz+dz]
        case 8: res=[px,py-dy,pz+dz]
    return res

def relJointPosFromDir(parentDims, pDir, dir): # relative to parent joint
    x, y, z = parentDims[0], parentDims[1], parentDims[2]
    match pDir:
        case 0:
            match dir:
                case 0: res=[0,0,z]
                case 1: res=[x/2,0,z/2]
                case 2: res=[-x/2,0,z/2]
                case 3: res=[0,y/2,z/2]
                case 4: res=[0,-y/2,z/2]
                case 5: res=[x/2,0,z]
                case 6: res=[-x/2,0,z]
                case 7: res=[0,y/2,z]
                case 8: res=[0,-y/2,z]
        case 1:
            match dir:
                case 0: res=[x/2,0,z/2]
                case 1: res=[x,0,0]
                case 2: res=None # would cause intersecting links
                case 3: res=[x/2,y/2,0]
                case 4: res=[x/2,-y/2,0]
                case 5: res=[x,0,z/2]
                case 6: res=[0,0,z/2] # might want to remove
                case 7: res=[x/2,y/2,z/2]
                case 8: res=[x/2,-y/2,z/2]
        case 2:
            match dir:
                case 0: res=[-x/2,0,z/2]
                case 1: res=None
                case 2: res=[-x,0,0]
                case 3: res=[-x/2,y/2,0]
                case 4: res=[-x/2,-y/2,0]
                case 5: res=[0,0,z/2] # might want to remove
                case 6: res=[-x,0,z/2] 
                case 7: res=[-x/2,y/2,z/2]
                case 8: res=[-x/2,-y/2,z/2]
        case 3:
            match dir:
                case 0: res=[0,y/2,z/2]
                case 1: res=[x/2,y/2,0]
                case 2: res=[-x/2,y/2,0]
                case 3: res=[0,y,0]
                case 4: res=None
                case 5: res=[x/2,y/2,z/2]
                case 6: res=[-x/2,y/2,z/2] 
                case 7: res=[0,y,z/2]
                case 8: res=[0,0,z/2] # might want to remove
        case 4:
            match dir:
                case 0: res=[0,-y/2,z/2]
                case 1: res=[x/2,-y/2,0]
                case 2: res=[-x/2,-y/2,0]
                case 3: res=None
                case 4: res=[0,-y,0]
                case 5: res=[x/2,-y/2,z/2]
                case 6: res=[-x/2,-y/2,z/2] 
                case 7: res=[0,0,z/2]
                case 8: res=[0,-y,z/2] 
        case 5:
            match dir:
                case 0: res=[x/2,0,z]
                case 1: res=[x,0,z/2]
                case 2: res=[0,0,z/2] # might want to remove
                case 3: res=[x/2,y/2,z/2]
                case 4: res=[x/2,-y/2,z/2]
                case 5: res=[x,0,z]
                case 6: res=[0,0,z] 
                case 7: res=[x/2,y/2,z]
                case 8: res=[x/2,-y/2,z] 
        case 6:
            match dir:
                case 0: res=[-x/2,0,z]
                case 1: res=[0,0,z/2] # might want to remove
                case 2: res=[-x,0,z/2] 
                case 3: res=[-x/2,y/2,z/2]
                case 4: res=[-x/2,-y/2,z/2]
                case 5: res=[-x,0,z]
                case 6: res=[0,0,z] 
                case 7: res=[-x/2,y/2,z]
                case 8: res=[-x/2,-y/2,z] 
        case 7:
            match dir:
                case 0: res=[0,y/2,z]
                case 1: res=[x/2,y/2,z/2] 
                case 2: res=[-x/2,y/2,z/2] 
                case 3: res=[0,y,z/2]
                case 4: res=[0,0,z/2]
                case 5: res=[x/2,y/2,z]
                case 6: res=[-x/2,y/2,z] 
                case 7: res=[0,y,z]
                case 8: res=[0,0,z] 
        case 8:
            match dir:
                case 0: res=[0,-y/2,z]
                case 1: res=[x/2,-y/2,z/2] 
                case 2: res=[-x/2,-y/2,z/2] 
                case 3: res=[0,0,z/2]
                case 4: res=[0,-y,z/2]
                case 5: res=[x/2,-y/2,z]
                case 6: res=[-x/2,-y/2,z] 
                case 7: res=[0,0,z]
                case 8: res=[0,-y,z] 
    return res

def relLinkPosFromDir(dims, dir): # relative to parent joint
    x, y, z = dims[0], dims[1], dims[2]
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