arr = range(10)
arr2 = list(range(10))	#range函数只是生成一个整数序列，需要配合 list 来生成一个队列

	
print(arr)
print(arr2)

sum = 0
for x in list(range(101)):
	sum = sum + x

print('计算0到100的累加')
print(sum)