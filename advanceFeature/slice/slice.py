L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#取前三个元素，应该怎么做
#笨方法：[L[0], L[1], L[2]]

#取前N个元素呢？
r = []
n = 3
for i in range(n):
	r.append(L[i])
print(r)

#对于上面的问题可以用一行代码完成 “切片”
print(L[0:3])
print(L[1:2])