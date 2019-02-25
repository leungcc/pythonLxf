#创建set的参数是一个list
s = set([1, 2, 3, 3, 1])
#重复的元素在set中自动被过滤
print(s)	

#通过add(key)方法可以添加元素到set中
s.add(4)
print(s)

#通过remove(key)方法可以删除元素
s.remove(4)
print(s)

#set可以看成数学意义上的无序和无重复元素的集合，
#因此两个set可以做数学意义上的交集、并集等操作
s1 = set([1, 2, 3]);
s2 = set([2, 3, 4]);
print(s1 & s2)
print(s1 | s2)
