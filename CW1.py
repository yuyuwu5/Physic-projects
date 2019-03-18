#ex1
from __future__ import division, print_function
from visual import *
scene_eg1=display(title='First Program') # Create a scene
sphere(pos=vector(-10, 0, 0), radius = 2.5, color = color.green)
sphere(pos=vector(0, 0, -5), radius = 1.5, color = color.green)
sphere(pos=vector(0, -10, 0), radius = 2.5, color = color.green)
arrow(pos=vector(-10, 0 ,0) axis = vector(3, 2, -1 ), color = color.red)
arrow(pos=vector(0, 0 ,-5) axis = vector(2, -4, 0 ), color = color.red)
arrow(pos=vector(0, -10 ,0) axis = vector(-3, 2, 1 ), color = color.red)

#ex2
from __future__ import division, print_function
from visual import *
scene_eg2=display(title='Naming Objects and Variables') # Create a scene 
a = sphere(pos=vector(-1,0,0),radius=0.25, color=color.red) 
b = sphere(pos=vector(1,1,0),radius=0.15, color=color.orange) 
arrow(pos= a.pos,axis=b.pos - a.pos,color=color.yellow)

#ex3
from visual import *
scene_eg3=display(title='Syntax Errors') # Create a scene 
Bob=sphere(pos=vector(-1,-1,-1), radius=0.4, color=color.red) 
Lucy=sphere(pos=vector(1,0,0), radius=0.4, color=color.green) 
arrow(pos=Bob.pos, axis=vector(1,-1,0), color=color.magenta)

#ex4
from __future__ import division, print_function
from visual import *
scene_eg4 = display(title='Using comments') #create another scene 
Bob=sphere(pos=vector(-1,-1,-1), radius=0.4, color=color.red) #Bob is a ball
Lucy=sphere(pos=vector(1,0,0), radius=0.4, color=color.green) #Lucy is also a ball
arrow(pos=Bob.pos, axis=vector(-0.5,0.5,0), color=color.magenta)
