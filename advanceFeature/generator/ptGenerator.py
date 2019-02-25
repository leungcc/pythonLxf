#写一个generator可以输出第n行整行的 list

def ptGenerator(num):
	result = [[1], [1, 1]]
	n = 3
	while n <= num:
		cur = []
		preLine = result[n-2]
		for x in range(n):
			#a, b = preLine[x-1], preLine[x]
			# a = x - 1 > -1 ? preLine[x-1] : 0;
			# b = x >= len(preLine) ? 0 : preLine[x]
			a = preLine[x-1] if x-1>=0 else 0
			b = preLine[x] if x<len(preLine) else 0
			cur.append(a+b)
		result.append(cur)
		n += 1

		yield cur;


g = ptGenerator(6)

for x in g:
	print(x)
