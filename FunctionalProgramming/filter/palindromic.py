def allNum():
	num = 0
	while True:
		yield num
		num += 1

#回文数
def palindromic():
	#得到全体自然数 generator allnum
	allnum = allNum()
	#遍历全体自然数
	for num in allnum:
		numStr = str(num)
		numLen = len(numStr)
		flag = True
		#遍历该自然数各个位上的数字
		for i in range(len(numStr)):
			if(numStr[i] != numStr[numLen-i-1]):
				flag = False
				break;
		if(flag):
			yield num


palinIt = palindromic()


#输出排第n个回文数
def getNpalin(n):
	index = 1
	for x in palindromic():
		if(index == n):
			print(x)
			break;
		index += 1

#打印数字小于n的回文数
def printAllPalin(n):
	for x in palindromic():
		print(x)
		if x > n:
			break;

getNpalin(100)
printAllPalin(10)
