#参数检查
#python内置函数如abs()传入str会报错TypeError: bad operand type for abs():'str'

#但如果我们的 my_abs()会报错 TypeError: unorable types: str() >= int()
#让我们修改一下 my_abs()，对参数进行检查，只允许整数和浮点数类型的参数

def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x>=0:
		return x
	else:
		return -x
print(my_abs(-11))
print(my_abs('abc'))
