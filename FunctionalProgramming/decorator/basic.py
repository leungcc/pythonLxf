#decorator本质上是一个返回函数的高阶函数。
#定义一个能打印日志的decorator：
def log(func):
	def wrapper(*args, **kw):
		print('call %s():' %func.__name__)
		return func(*args, **kw);
	return wrapper;

#因为decorator接受一个函数作为参数，并返回一个函数。
#所以我们借助Python的 @语法，把decorate置于函数的定义处
@log
def now():
	print('2015-3-25')

now();