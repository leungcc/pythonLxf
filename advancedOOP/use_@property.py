#先来温习一下 decorator 的用法
import functools;
import datetime;

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print(datetime.datetime.now().strftime('%F %T'))
		return func(*args, **kw)
	return wrapper

@log
def printHello():
	print('Hello')

printHello();


#=================================================================================
#现在说新知识点--@property
class Student(object):

	def __init__(self, score):
		self._score = score

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value;

xc = Student(111);
print(xc.score);
xc.score = 88;
print(xc.score);
#xc.score = 10086;
#print(xc.score);


	