from hello import Hello

class Dog(object):
	def __init__(self, name):
		self.name = name

h = Hello();
h.hello();

print(type(Hello))		#<class 'type'>
print(type(Dog))		#<class 'type'>