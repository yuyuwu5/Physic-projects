from visual import*
import random,time,math
scene.width = 650
scene.height = 650
scene.forward=vector(0,1,0)
scene.center=vector(0,0,5)
scene.range=(30,30,30)

center=sphere(pos=vector(0,0,10),radius=2,color=color.blue)
cap=sphere(pos=center.pos,radius=13,color=color.white,opacity=0.3)
cylinder(pos=vector(0,0,-10),axis=vector(0,0,20),radius=1,material=materials.silver)
box(pos=vector(0,0,-10),height=50,length=50,width=1,material=materials.wood)
local_light(pos=(0,0,0), color=color.yellow)
theta=pi/3
target=sphere(pos=vector(center.pos.x+1.15*cap.radius*cos(theta),center.pos.y,center.pos.z+1.15*cap.radius*sin(theta)),radius=center.radius,color=color.red)

max_node=50000
count=0
delta=1.5
node=[]
distant_light(direction=(-0.78, -0.22, -0.44), color=color.gray(0.3))
class Node(object):
	def __init__(self, now, parent):
		self.now = now
		self.parent = parent

def distance(p1,p2):
	return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def reach(now,target):
	if distance(now,target)<=center.radius+0.2:
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
		
root=Node(center.pos,None)
node.append(root)

text=label(pos=(3,-42,0), text='Click to remove RRT tree after reach')
path=frame()
scene.waitfor('click')
while True: 
	rate(200)
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
	curve(pos=[node1,parents.now],radius=0.05,color=color.green,frame=path)
	curve(pos=[node2,parents.now],radius=0.05,color=color.cyan,frame=path)
	curve(pos=[node3,parents.now],radius=0.05,color=color.blue,frame=path)
	goal=None
	if reach(node1,target.pos):
		goal=node[len(node)-3]
	elif reach(node2,target.pos): 
		goal=node[len(node)-2]
	elif reach(node3,target.pos):
		goal=node[len(node)-1]
	if scene.mouse.clicked:
		text.visible=False
	if goal!=None:
		print('reach')
		if scene.mouse.clicked:
			time.sleep(1)
			path.visible=False
		while goal.parent!=None:
			curve(pos=[goal.now,goal.parent.now],radius=0.07)
			goal=goal.parent
		break