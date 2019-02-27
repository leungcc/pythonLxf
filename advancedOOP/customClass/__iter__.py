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


#打印斐波那契数列
fib = Fib()
for i in fib:
	print(i)
