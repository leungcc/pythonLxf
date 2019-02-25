#解决循环闭包的问题
def count():
	fs = []
	for i in range(1, 4):
		def f(index):
			def ff():
				return index*index
			return ff;

		fs.append(f(i))
	return fs

f1, f2, f3 = count()


print(f1())		#1
print(f2())		#4
print(f3())		#9


#使用匿名函数可以简化代码
def count2():
	fs = []
	for i in range(1, 4):
		def f(index):
			return lambda: index*index;

		fs.append(f(i))
	return fs

f1, f2, f3 = count2()
print(f1())		#1
print(f2())		#4
print(f3())		#9