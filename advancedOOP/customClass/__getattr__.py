class Student(object):
	def __init__(self, name):
		self.name = name
	def __getattr__(self, attr):
		if attr != 'name':
			return None;

xc = Student('xc')
print(xc.name)
print(xc.score)


#这方法可以把一个类的所有属性和方法调用全部动态化处理了
class Chain(object):
	def __init__(self, path='face-manage'):
		self._path = path
	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))
	def __str__(self):
		return self._path

	__repr__ = __str__;

print(Chain().api.weixin)
print(Chain().status.user.timeline.list)