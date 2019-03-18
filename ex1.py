from __future__ import division, print_function
from visual import *
scene_eg1=display(title='First Program') # Create a scene
sphere(pos=vector(-10, 0, 0), radius = 2.5, color = color.green)
sphere(pos=vector(0, 0, -5), radius = 1.5, color = color.green)
sphere(pos=vector(0, -10, 0), radius = 2.5, color = color.green)
arrow(pos=vector(-10, 0 ,0) axis = vector(3, 2, -1 ), color = color.red)
arrow(pos=vector(0, 0 ,-5) axis = vector(2, -4, 0 ), color = color.red)
arrow(pos=vector(0, -10 ,0) axis = vector(-3, 2, 1 ), color = color.red)