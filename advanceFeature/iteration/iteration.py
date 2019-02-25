#迭代list或者tuple
for x in range(10):
	print(x)    #打印数组元素

#迭代dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)	#打印的是key

print('-----print d.value()', ':', d.values())
print(isinstance(d.values(), (list, tuple)))  #这里竟然是False

for value in d.values():
	print(value)

#如果要同时迭代key和value：
print('print for key,value in d.items():')
for key, vlaue in d.items():
	print(key, ':', value)