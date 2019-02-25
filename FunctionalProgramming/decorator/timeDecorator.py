import datetime
import functools
#输出当前时间
#print(datetime.datetime.now().strftime('%F %T'))
#decorator log 可以作用于任何函数，打印该函数的执行时间

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print(datetime.datetime.now().strftime('%F %T'))
		return func(*args, **kw);
	return wrapper;

@log
def printHello():
	print('Hello')

printHello();
