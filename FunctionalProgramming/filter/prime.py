def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_dvisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()  #初始化序列
	while True:
		n = next(it)  #返回序列的第一个数
		yield n
		it = filter(_not_dvisible(n), it)  #构造新序列

for n in primes():
	if n < 1000:
		print(n)
	else:
		break;

# def test():

# 	it = filter(lambda x: x < 100, _odd_iter())
# 	print(next(it))
# 	it = filter(lambda x: x != 10, it)
# 	print(next(it))

# test()