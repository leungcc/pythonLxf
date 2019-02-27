import types;

print('use type(xxx) ----------')
print(type(123))		#  <class 'int'>
print(type('str'))		#  <class 'str'>
print(type(None))		#  <class 'NoneType'>
print(type(abs))		#  <class 'buildin_function_or_method'>
#print(haha)				#报错，python没有变量提升（区别于javascript）

def haha(name):
	print(name + ' is haha')

class Animal(object):
    def run(self):
        print('Animal is running...')
print(type(haha))		#  <class 'function'>
print(haha)				#  <function haha at 0x000000228BE36C1E0>
print(type(Animal()))


print('use types.xxx ----------')
#print(types.BuiltinFunctionType)		#跟type(abs)一样  <class 'buildin_function_or_method'>
#print(types.FunctionType)				#跟type(haha)一样  <class 'function'>

print('types.BuiltinFunctionType: ', types.BuiltinFunctionType) #fn
print('types.FunctionType: ', types.FunctionType)		#abs
print('types.LambdaType: ', types.LambdaType)			#lambda x: x
print('types.GeneratorType: ', types.GeneratorType)		#x for x in range(10)
