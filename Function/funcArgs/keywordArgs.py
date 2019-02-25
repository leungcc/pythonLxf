def person(name, age, **kw):
	print('name', name, 'age', age, 'other', kw)

person('xcleung', 24, city='Guangzhou')

dict1 = {'city': 'Guangzhou', 'height': 175}
person('xcleung', 24, **dict1)

