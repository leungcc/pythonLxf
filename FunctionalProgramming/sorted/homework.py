L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)];
def sortFn(item):
	return item[1]

print(sorted(L, key=sortFn))