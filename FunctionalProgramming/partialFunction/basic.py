import functools
int2 = functools.partial(int, base=2)

print(int2('11'))		#3
print(int2('110'))		#6