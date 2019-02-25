def power(x, n):
	s = 1
	while n>0:
		s = x*s
		n = n-1
	return s

print(power(2, 3))	#8