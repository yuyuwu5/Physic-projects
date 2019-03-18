from visual import *
from visual.graph import *
import math 

scene.width = 650
scene.height = 700
scene.autoscale = True 
scene.userzoom = True
scene.center = vector(0,13,0)  

print("key in theta (0~180)")
A=input("")
theta = pi/180*A
print("key in 0, 1 or 2 (0 for no rotation; 1 for constant speed of rotation; 2 for acceleration of speed of rotation)")
situation=input("")
if situation == 0:
	scene.title='no rotation'
elif situation == 1:
	scene.title='constant speed of rotation'
else:
	scene.title='acceleration of speed of rotation'

gyroscope=frame()
floor= box(pos=vector(0,0,0),width=50, height = 1, length =50, color=vector(0.3,0.6,0.5),material=materials.rough)
shelf1= cylinder(pos= vector(0,1,0), axis = vector(0,1,0),radius = 12,color=color.orange,material=materials.wood)
shelf2= cylinder(pos= shelf1.pos+shelf1.axis, axis = vector(0,10,0),radius = 1.5, color=color.orange,material=materials.wood)
axle_start=sphere(pos=shelf2.pos+shelf2.axis, radius = 0.6,color=color.cyan,frame=gyroscope )
axle_end=sphere(pos=shelf2.pos+shelf2.axis+24*vector(cos(theta),sin(theta),0), radius = 0.6,color=color.cyan,make_trail=True,frame=gyroscope,retain=500)
axle = cylinder(pos= axle_start.pos, axis= axle_end.pos-axle_start.pos, 
	            radius = 0.5, color = color.white,frame=gyroscope )
plate = cylinder(pos= axle_start.pos+(axle_end.pos-axle_start.pos)/2-vector(cos(theta),sin(theta),0), 
	             axis = 2*vector(cos(theta),sin(theta),0),radius = 8,color=color.yellow,material=materials.shiny,frame=gyroscope)
horizontal_ring=ring(pos=plate.pos+vector(cos(theta),sin(theta),0), axis=2*vector(cos(theta),sin(theta),0), radius=9.5, thickness=0.5,color=color.white,frame=gyroscope)
vertical_ring=ring(pos=plate.pos+vector(cos(theta),sin(theta),0), axis=2*vector(sin(theta),-cos(theta),0), radius=9.5, thickness=0.5,color=color.white,frame=gyroscope)

L_arrow=arrow(pos=plate.pos,axis=vector(0,0,0),color=color.red,shaftwidth=0.8)
dL_arrow=arrow(pos=L_arrow.pos+L_arrow.axis,axis=vector(0,0,0),color=color.yellow,shaftwidth=0.3)
g_arrow=arrow(pos=plate.pos,axis=vector(0,0,0),color=color.magenta,shaftwidth=0.8)
L_arrow.visible=False
dL_arrow.visible=False
g_arrow.visible=False

g1=gdisplay(width=400,height=200,title='w vs t',ytitle='w',xtitle='time') 
gc11=gcurve(gdisplay=g1,color=color.green,dot=True) 


label1=label(pos=(20,-20,0), text='Click to start')

if A != 90:
    g2=gdisplay(width=400,height=200,title='w_precession vs t',ytitle='w_pre',xtitle='time') 
    gc21=gcurve(gdisplay=g2,color=color.blue,dot=True) 

g=9.80665
m=1
R=(axle_end.pos-axle_start.pos)/2
dt=0.01
t=0

I= 0.5*m*plate.radius**2

def gravity (tow, m, R,t) :
 	v=abs(R)*vector(cos(0.5*(2*theta-abs(tow)/(m*abs(R)**2)*t**2)-5/180),sin(0.5*(2*theta-abs(tow)/(m*abs(R)**2)*t**2)-5/180),0)+vector(0,shelf2.pos.y+shelf2.axis.y-1,0)
        return v

print('click to start')      
scene.waitfor('click')

label1.visible=False
label2=label(pos=(20,-20,0), text='Click to show arrow')

while True:
    rate(100)
    if situation == 0:
        a = 0
    elif situation == 1:
        a = pi*2/100
    else:
        a = pi*2/100+0.005*t
    F = m*g*vector(0,-1,0)
    R =(axle_end.pos-axle_start.pos)/2
    tow=cross(R,F)
    if a<= 0.008:
        falling_time = 0
        while axle_end.pos.y > 10:
            rate(100)
            axle_end.pos=gravity(tow,m,2*R,falling_time)
            axle.axis=abs(axle.axis)*norm(axle_end.pos-axle_start.pos)
            axle_end.pos=axle.pos+axle.axis
            plate.pos=axle.pos+0.5*(axle.axis)-vector(cos(theta),sin(theta),0)
            plate.axis=abs(plate.axis)*norm(axle.axis)
            vertical_ring.pos=plate.pos+vector(cos(theta),sin(theta),0)
            horizontal_ring.pos=plate.pos+vector(cos(theta),sin(theta),0)
            horizontal_ring.axis=plate.axis
            vertical_ring.axis=vector(-plate.axis.y,plate.axis.x,0)
            falling_time += dt
    else:
        w=100*a
        L = (I*w)*norm(axle.axis)
        F = m*g*vector(0,-1,0)
        R =plate.pos-axle_start.pos
        tow=cross(R,F)
        w_pre=m*abs(R)*g/(I*w)
        dl = tow*dt
        L += dl
        axle_end.pos=axle_start.pos+abs(axle.axis)*norm(L)
        plate.pos = axle_start.pos+0.5*abs(axle.axis)*norm(L)
        horizontal_ring.pos=axle_start.pos+0.5*(abs(axle.axis)+2)*norm(L)
        vertical_ring.pos=axle_start.pos+0.5*(abs(axle.axis)+2)*norm(L)
        axle.axis=axle_end.pos-axle_start.pos
        plate.axis=norm(axle.axis)*abs(plate.axis)
        horizontal_ring.axis=plate.axis   
        plate.rotate(angle=a)
        horizontal_ring.rotate(angle=a)
        vertical_ring.rotate(angle=a,axis=axle.axis)
        if scene.mouse.clicked:
        	L_arrow.visible=True
        	g_arrow.visible=True
        	if theta != pi/2:
        		dL_arrow.visible=True	
        L_arrow.axis=norm(L)*20
        L_arrow.pos=plate.pos
        g_arrow.pos=plate.pos
        g_arrow.axis=F
        dL_arrow.pos=L_arrow.pos+L_arrow.axis
        dL_arrow.axis=norm(dl)
        gc11.plot(pos=(t,w))
        if A !=90:
            gc21.plot(pos=(t,w_pre))
    if axle_end.pos.y < 10:
    	break
    t += dt  
