from visual import*
from math import*
import random,time
scene.width = 650
scene.height = 650
scene.forward=vector(0,1,0)
scene.center=vector(0,0,5)
scene.range=(30,30,30)

max_node=50000
count=0
delta=random.randint(1,9)
node=[]

class Node(object):
	def __init__(self, now, parent):
		self.now = now
		self.parent = parent

def distance(p1,p2):
	return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def reach_ground(now,target):
	if now[2]-target[2] < 0.5:
		return True
	return False
def random_pos():
	return random.randint(-100,101),random.randint(-100,101),random.randint(-100,101)

def explore(p1,p2):
	distance_=distance(p1,p2)
	if distance_< delta:return p2
	else:
		phi=atan2(p2[2]-p1[2],sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2))
		theta=atan2(p2[1]-p1[1],p2[0]-p1[0])
		return p1[0]+delta*cos(phi)*cos(theta),p1[1]+delta*cos(phi)*sin(theta),p1[2]+sin(phi)*delta
		
sky=box(pos=vector(0,0,25),height=50,length=50,width=1,color=color.blue)
ground=box(pos=vector(0,0,-15),height=50,length=50,width=1,color=color.red)
tmp=vector(random.randint(-10,10),random.randint(-10,10),25)
root=Node(tmp,None)
node.append(root)
local_light(pos=ground.pos, color=color.yellow)

path=frame()
scene.waitfor('click')
while True: 
	rate(1000)
	count+=1
	if count <= max_node:
		find_next=False
		while find_next==False:
			r1=random_pos()
			r2=random_pos()
			r3=random_pos()
			parents=node[0]
			for vertex in node:
				if distance(vertex.now,r1)<=distance(parents.now,r1) and distance(vertex.now,r2)<=distance(parents.now,r2) and distance(vertex.now,r3)<=distance(parents.now,r3):
					parents=vertex
					find_next=True
	node1=explore(parents.now,r1)
	node2=explore(parents.now,r2)
	node3=explore(parents.now,r3)
	node.append(Node(node1,parents))
	node.append(Node(node2,parents))
	node.append(Node(node3,parents))
	goal=None
	if reach_ground(node1,ground.pos):
		goal=node[len(node)-3]
	elif reach_ground(node2,ground.pos): 
		goal=node[len(node)-2]
	elif reach_ground(node3,ground.pos):
		goal=node[len(node)-1]
	if goal!=None:
		for obj in scene.objects: 
			if isinstance(obj, curve):	
				obj.visible=False
				del obj
		print('reach')
		lightning=curve(pos=[goal.now],radius=0.07,color=color.white)
		while goal.parent!=None:
			lightning.append(pos=goal.parent.now)
			goal=goal.parent
		time.sleep(0.5)
		del node
		node=[]
		tmp=vector(random.randint(-25,25),random.randint(-25,25),25)
		root=Node(tmp,None)
		node.append(root)
		count=0
		delta=random.randint(1,9)
