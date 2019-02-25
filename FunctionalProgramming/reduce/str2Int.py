from functools import reduce
from collections import Iterator
from collections import Iterable

DIGITS = {
	'0':0, '1':1, '2':2, '3':3,'4':4, 
	'5':5, '6':6, '7':7, '8':8, '9':9
}

def str2int(s):
	def fn(x, y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))

def char2num(s):
	return DIGITS[s]

print('map函数返回', map(char2num, '12345'))
print('list(map函数返回)', list(map(char2num, '12345')))
print('isinstance(map(char2num, "12345"), (Iterable))', isinstance(map(char2num, '12345'), (Iterable)))
print('isinstance(map(char2num, "12345"), (Iterator))', isinstance(map(char2num, '12345'), (Iterator)))