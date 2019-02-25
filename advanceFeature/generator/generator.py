g = (x*x for x in range(1,11))

print(g)	#<generator object <genexpr> at 0x0000012A8F200C78

for x in g:
	print(x)