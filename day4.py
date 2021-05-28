q = 1
while q <= 7:
    k=7
    while k>=q:
        j = 1
        print(" ",end="")
        k=k-1
    while j<=q:
        print("* ",end="")
        j = j+1
    print()
    q = q+1

执行结果：
1
2
3
4
5

a =["北京","上海","广东"]
a.append("石家庄")
a.append("郑州")
a.append("哈尔滨")
a[1]="广东"
a[2]="上海"
print(a)

b=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
print(sum(b)/len(b))



a = [1, 5, 21, 30, 15, 9, 30, 24]
i= 0
s= 0
num =0
while i<=7:
    i=i+1
    if  a[num] % 5 == 0:
        s = s+a[num]
        num=num+1
    else:
        num = num+1
print(s)


list=[1,2,3,4,5,6,7,8,9]
list.reverse()
print(list)


list=[1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a=list.count(1)
b=list.count(2)
c=list.count(3)
d=list.count(4)
e=list.count(5)
f=list.count(6)
g=list.count(7)
h=list.count(8)
i=list.count(9)
j=list.count(10)
print("1出现的次数为：",a)
print("2出现的次数为：",b)
print("3出现的次数为：",c)
print("4出现的次数为：",d)
print("5出现的次数为：",e)
print("6出现的次数为：",f)
print("7出现的次数为：",g)
print("8出现的次数为：",h)
print("9出现的次数为：",i)
print("10出现的次数为：",j)