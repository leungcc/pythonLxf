n = 0
while n < 10:
	n = n + 1
	print(n)

#上面的程序可以打印1-10，假如我们只想打印奇数，
#可以用 continue 语句跳过某些循环
#
print('-------')
print('下面只打印10以内的奇数')

i = 0
while i < 10:
	i = i + 1
	if i%2 == 0:
		continue
	print(i)