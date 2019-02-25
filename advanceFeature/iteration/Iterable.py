from collections import Iterable

print(isinstance('abc', Iterable));		#True
print(isinstance(123, Iterable));		#False

#如果要对list实现类似Java那样的下表循环怎么办？
#Python内置的 enumerate 函数可以把一个list变成索引-元素对
enum = enumerate(['A', 'B', 'C'])
print(enum)
for i,value in enum:
	print(i, ':', value)