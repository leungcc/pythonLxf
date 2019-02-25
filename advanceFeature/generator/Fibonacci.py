def fib(num):
	n, x, y = 0, 0, 1
	while(n < num):
		# oldX = x
		# x = y
		# y = oldX + y
		x, y = y, x+y  #这样就不用写中间变量oldX
		print(x)
		n += 1

fib(6)