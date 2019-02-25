from functools import reduce

L = [1,3,5,7,9]

def fn(x, y):
	return x*10 + y


print(reduce(fn, L))