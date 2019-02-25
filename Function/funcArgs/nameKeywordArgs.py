def person(name, age, *, city):
	print(name, age, city)

person('xcleung', 24, **{'city': 'Guangzhou', 'job': 'Engineer'})
person('xcleung', 24, city='Guangzhou')

