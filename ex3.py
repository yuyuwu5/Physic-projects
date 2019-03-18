from visual import *
scene_eg3=display(title='Syntax Errors') # Create a scene 
Bob=sphere(pos=vector(-1,-1,-1), radius=0.4, color=color.red) 
Lucy=sphere(pos=vector(1,0,0), radius=0.4, color=color.green) 
arrow(pos=Bob.pos, axis=vector(1,-1,0), color=color.magenta)
