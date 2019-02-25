#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
	num = 0
	def reFn():
		nonlocal num		#调用外层函数的变量需要用 nonlocal关键字声明
		num += 1;
		return num
	return reFn

jishuqi = createCounter();

print(jishuqi())
print(jishuqi())