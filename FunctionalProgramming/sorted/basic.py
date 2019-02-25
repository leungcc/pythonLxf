#最基础用法
print( sorted([36, 5, -12, 9, 21]) )

#加入key命名关键字参数
print( sorted([36, 5, -12, 9, 21], key=abs) )

#字符串排序默认按照 ASCII 的大小比较的，由于'Z'<'a'，所以大写字母Z会排在小写字母a前面
print( sorted(['bob', 'about', 'aaaaa', 'Zoo', 'Credit']) )

#现在我们提出排序要忽略大小写
print( sorted(['bob', 'about', 'aaaaa', 'Zoo', 'Credit'], key=str.lower) )

#要进行反向排序，不必改动key函数，可以传入第三个参数 reverse=True
print( sorted([36, 5, -12, 9, 21], reverse=True) )
