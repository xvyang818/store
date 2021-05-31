w = ['小明','小张','小黄','小杨',]
y = ['小黄','小李','小王','小杨','小周']
z = ['小杨','小张','小吴','小冯','小周']

total = set(w + y + z)
print(len(total))

first = []
for student in w:
    if student not in y and student not in z:
        first.append(student)
print('只选了第一个学科的数量为{}，名字为{}'.format(len(first), first))

group = {}
ALL = w + y + z
for student in total:
    if student not in group:
        group[student] = ALL.count(student)
print(group)

n=1
for a in w:
    if a in z and a not in y:
        n = n + 1
        print(n)


i=9
while i > 0:
    j=1
    while j <= i:
        print(j,"x",i,"=",(j*i)," ",end="")
        j = j + 1
    print()
    i = i - 1