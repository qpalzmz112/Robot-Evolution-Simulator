import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5
for k in range(5):
	for j in range(5):
		for i in range(10):
			pyrosim.Send_Cube(name="Box", pos=[x+j,y+k,i + .5] , size=[length * 0.9**i, width * 0.9**i, height * 0.9**i])
pyrosim.End()