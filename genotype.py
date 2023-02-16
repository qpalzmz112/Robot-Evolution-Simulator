import pyrosim.pyrosim as pyrosim

class NODE:
    def __init__(self, name, dims, pos, sens):
        self.name = name
        self.dims = dims
        self.pos = pos
        self.sens = sens
        self.children = []

    def Add_Child(self, node):
        self.children.append(node)

    def Send_Link(self, col):
        pyrosim.Send_Cube(name=self.name, pos=self.pos, size=self.dims, color=col)

    def Joint_Pos_From_Dir(self, dir):
        match dir:
            case 0: res=[self.pos[0],self.pos[1],self.pos[2]+self.dims[2]/2]
            case 1: res=[self.pos[0]+self.dims[0]/2,self.pos[1],self.pos[2]]
            case 2: res=[self.pos[0]-self.dims[0]/2,self.pos[1],self.pos[2]]
            case 3: res=[self.pos[0],self.pos[1]+self.dims[1]/2,self.pos[2]]
            case 4: res=[self.pos[0],self.pos[1]-self.dims[1]/2,self.pos[2]]
            case 5: res=[self.pos[0]+self.dims[0]/2,self.pos[1],self.pos[2]+self.dims[2]/2]
            case 6: res=[self.pos[0]-self.dims[0]/2,self.pos[1],self.pos[2]+self.dims[2]/2]
            case 7: res=[self.pos[0],self.pos[1]+self.dims[1]/2,self.pos[2]+self.dims[2]/2]
            case 8: res=[self.pos[0],self.pos[1]-self.dims[1]/2,self.pos[2]+self.dims[2]/2]
        return res