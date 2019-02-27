class Student(object):
	def __init__(self, name):
		self.name = name

print(Student('xc'));	#<__main__.Student object at 0x109afb190>


#像上面一样打印这个实例，很难看！
#现在我们用 __str__ 看看效果

class GoodStudent(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return 'Student object (name:%s, age:%s)' %(self.name, self.age)

print(GoodStudent('xc', 25))