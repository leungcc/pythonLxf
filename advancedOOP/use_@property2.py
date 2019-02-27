class Student(object):

	@property
	def birth(self):
		return self._birth;

	@birth.setter
	def birth(self, value):
		self._birth = value;

	@property
	def age(self):
		return 2019 - self._birth;

xc = Student();
xc.birth = 1994;
print(xc.age)
#xc.age = 99		#报错，age没有 @age.setter，则为只读
	
	