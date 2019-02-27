class Animal(object):

    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Husky(Dog):
	
	def destroy(self):
		print('WaWhoo, ~~ boom!boom!boom!!');



#判断参数是否是类型的其中一种
print('isinstance(123, (tuple, list))', isinstance(123, (tuple, list)))
print('isinstance(123, (int, list))', isinstance(123, (int, list)))