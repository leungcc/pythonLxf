#请定义一个函数 quadratic(a, b, c)，接受3个参数，返回一元二次方程ax2+bx+c=0的两个解
import math;

def quadratic(a, b, c):
	if (not isinstance(a, (int))) | (not isinstance(b, (int))) | (not isinstance(c, (int))):
		raise TypeError('quadratic request args of int')
	
	deita = b*b - 4*a*c
	print('deita=', deita)

	if deita > 0:
		x1 = (-b + math.sqrt(deita))/(2*a);
		x2 = (-b - math.sqrt(deita))/(2*a);
		return x1, x2
	elif deita == 0:
		x1 = x2 = (-b + math.sqrt(deita))/(2*a);
		return x1, x2
	else:
		print('该方程不存在解')

print(quadratic(1, 5, 6));		#(-2, -3)
print(quadratic(1, 1, 6));		#该方程不存在解