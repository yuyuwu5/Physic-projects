from __future__ import division, print_function
from visual import *
scene_eg4 = display(title='Using comments') #create another scene 
Bob=sphere(pos=vector(-1,-1,-1), radius=0.4, color=color.red) #Bob is a ball
Lucy=sphere(pos=vector(1,0,0), radius=0.4, color=color.green) #Lucy is also a ball
arrow(pos=Bob.pos, axis=vector(-0.5,0.5,0), color=color.magenta)
