chinese = ['小明','小张','小黄','小杨',]
math = ['小黄','小李','小王','小杨','小周']
english = ['小杨','小张','小吴','小冯','小周']

a=[]
for index,value in enumerate(chinese):
    a.append(value)
for index,value in enumerate(math):
    if value in a:
        continue
    else:
        a.append(value)
for index,value in enumerate(english):
    if value in a:
        continue
    else:
        a.append(value)
print("总共有",len(a),"个学生选课")

d = []
for index,value in enumerate(a):
    if value not in math and value not in english:
        d.append(value)
print("只选了第一个科目的人为：",len(d),"对应的名字为：",d)

b = []
for index,value in enumerate(a):
    if (value in chinese and value in math) or (value in chinese and value in english) or (value in math and value in english):
        continue
    else:
        b.append(value)
print("只选了一个科目的人有",len(b),"他们的名单为：",b)

c = []
for index,value in enumerate(a):
    if value in chinese and value in math:
        c.append(value)
print("只选了语文和英语的数量为：",len(c),"对应的名字为：",c)