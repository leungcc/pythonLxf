import isinstance

print(dir('ABc'))

class MyObject(object):
	def __init__(self):
		self.__haha = 'hahahaha'
		self.x = 9
	def power(self):
		return self.x * self.x

obj = MyObject()

print(hasattr(obj, 'x'))			#True
print(hasattr(obj, 'y'))			#False
print(hasattr(obj, 'haha'))			#False (内部才能访问)
print(hasattr(obj, '__haha'))		#False
#print(obj.__haha)		# 直接报错