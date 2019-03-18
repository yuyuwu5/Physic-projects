from visual import*
import math,time

scene.width = 600
scene.height = 600
scene.range=(35,35,35)
scene.forward=vector(0,1,0)

origin=sphere(pos=vector(0,0,-35),radius=20,color=(0.5,1,0))
theta=(1./3)*pi
left=cylinder(pos=origin.pos+vector(-10,-3,20*cos(theta)),axis=1.5*vector(-10,0,23*cos(theta)),radius=1.5,material=materials.marble)
right=cylinder(pos=origin.pos+vector(10,0,20*cos(theta)),axis=1.5*vector(10,0,23*cos(theta)),radius=1.5,material=materials.marble)
helix(pos=left.pos,axis=0.8*left.axis,radius=left.radius+0.2,thickness=1.7,material=materials.marble)
helix(pos=right.pos,axis=0.8*right.axis,radius=right.radius+0.2,thickness=1.7,material=materials.marble)
positive=sphere(pos=left.pos+left.axis,color=color.red,radius=2*left.radius)
negative=sphere(pos=right.pos+right.axis,color=color.blue,radius=2*right.radius)
max_node=50000
count=0
delta=5
node=[]


class Node(object):
	def __init__(self, now, parent):
		self.now = now
		self.parent = parent

def distance(p1,p2):
	return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2+(p1[2]-p2[2])**2)

def reach(now,target):
	if distance(now,target)<=positive.radius+0.2:
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
		
root=Node(negative.pos,None)
node.append(root)

text=label(pos=(-3,-50,5), text='Click to remove RRT tree after reach')
distant_light(direction=vector(1,0,0), color=color.yellow)
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
	curve(pos=[node1,parents.now],radius=0.05,color=color.green,frame=path)
	curve(pos=[node2,parents.now],radius=0.05,color=color.cyan,frame=path)
	curve(pos=[node3,parents.now],radius=0.05,color=color.blue,frame=path)
	goal=None
	if reach(node1,positive.pos):
		goal=node[len(node)-3]
	elif reach(node2,positive.pos): 
		goal=node[len(node)-2]
	elif reach(node3,positive.pos):
		goal=node[len(node)-1]
	if scene.mouse.clicked:
		text.visible=False
	if goal!=None:
		print('reach')
		tmp=goal
		if scene.mouse.clicked:
			time.sleep(1)
			path.visible=False
		while goal.parent!=None:
			curve(pos=[goal.now,goal.parent.now],radius=0.1,material=materials.emissive)
			goal=goal.parent
		break

