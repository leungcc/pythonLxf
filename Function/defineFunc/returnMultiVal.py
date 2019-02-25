import math

def move(x, y, step, angle=0):
	nx = x + step*math.cos(angle)
	ny = y - step*math.sin(angle)
	return nx, ny

x, y = move(0, 0, 10, math.pi/4)
print(x, y)

haha = move(0, 0, 10, math.pi/4)
print(isinstance(haha, (tuple)))	#True