def is_odd(num):
    return num%2 == 1

result = filter(is_odd, [1,2,3,4,5]) #[]1,3,5]
print(list(result))

def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '   '])))