#定义一个函数计算两个数的乘积
def product(x, y):
	return x*y

print(product(2, 3))


#定义一个函数计算所有参数的乘积
def productN(*list):
	sum = 1
	for x in list:
		sum = sum*x
	return sum

print(productN(1,2,3,4))