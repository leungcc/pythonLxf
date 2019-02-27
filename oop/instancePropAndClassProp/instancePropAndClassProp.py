class Student(object):
	count = 0
	name = 'Student'
	def __init__(self, name):
		self.name = name
		Student.count+=1

s = Student('xc');
print(s.name);		#Student

print(Student.name);#Student
s.name = 'Michael';
print(s.name);		#Micheal

print(Student.name);#Student

del s.name;
print(s.name)		#Michael

Student('yy')
print(Student.count)#2

#从上面例子可以看出，在编写程序时，千万不要对实例属性和类属性使用相同得名字，
#因为相同名称的实例属性将屏蔽掉类属性，但当你删除实例属性后再使用相同的名称将访问到类属性