#杨辉三角算法：
#n是第n行，x是下标。 f(3,1) 就是第三行第2个元素
def f(n, x):
	if(n == 1):
		if(x == 0):
			return 1;
		else:
			return 0;
	elif(n == 2):
		if((x == 0) | (x == 1)):
			return 1;
		else:
			return 0;
	else:
		return f(n-1, x-1) + f(n-1, x);

print(f(6,2))
#print((1==1) | (1==2))