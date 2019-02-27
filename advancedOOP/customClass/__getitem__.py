
class Fib(object):
	def __init__(self):
		self.a, self.b = 0, 1
	def __iter__(self):
		return self			#本身就是迭代对象
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration();	#退出循环的条件
		return self.a		#返回下一个值

#Fib实例虽然能作用于 for 循环，看起来和list有点像，但是把它当成list来使用还是i不行
#print(Fib()[5])		#报错

class Fib2(object):
	def __getitem__(self, n):
		a, b = 1, 1
		for x in range(n):
			a, b = b, a + b
		return a

print(Fib2()[5])

#虽然上述实例已经可以使用    实例[index] 来取出index下标得元素，
#但 list还可以传入slice切片对象：
print( list(range(10))[0:3] )

#这时候要继续改造一下Fib类
class Fib3(object):
	def __getitem__(self, n):
		print(type(n))
		print(type([1:3]))
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a;
		elif isinstance(n, slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a, b = 1, 1
			L = []
			print('start', start)
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b = b, a + b
			return L;

print(Fib3()[3:5])