from visual import *
scene_eg2=display(title='Naming Objects and Variables') # Create a scene 
a = sphere(pos=vector(-1,0,0),radius=0.25, color=color.red) 
b = sphere(pos=vector(1,1,0),radius=0.15, color=color.orange) 
arrow(pos= a.pos,axis=b.pos - a.pos,color=color.yellow)

