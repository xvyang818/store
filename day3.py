a = input("一个数字：")
b = input("一个数字：")
c = input("一个数字：")
d = input("一个数字：")
e = input("一个数字：")
f = input("一个数字：")
g = input("一个数字：")
h = input("一个数字：")
i = input("一个数字：")
j = input("一个数字：")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
i = int(i)
j = int(j)
print("两个数的和为：",a+b+c+d+e+f+g+h+i+j)

a = input("一个数字：")
b = input("一个数字：")
c = input("一个数字：")
d = input("一个数字：")
e = input("一个数字：")
f = input("一个数字：")
g = input("一个数字：")
h = input("一个数字：")
i = input("一个数字：")
j = input("一个数字：")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
i = int(i)
j = int(j)
print("十个数的和为：",a+b+c+d+e+f+g+h+i+j)
print("平均数为：",(a+b+c+d+e+f+g+h+i+j)/10)
print("最大值为：")

import random
num = random.randint(50,150)
print(num)

a = input("请输入一个数：")
b = input("请输入一个数：")
c = input("请输入一个数：")
a = int(a)
b = int(b)
c = int(c)
if a == b == c:
    print("等边三角形")
elif a == b or a==c or b == c:
    print("等腰三角形")
elif a*a+b*b==c*c or a*a+c*c==b*b and b*b+c*c==a*a:
    print("直角三角形")
elif a +b >c and a-b >c:
    print("普通三角形")
elif a +b<c or a-b<c:
    print("不能构成三角形")

A = 56
B = 78
A = A + B
B = A - B
A = A - B
print(A)
print(B)

count = 3
while True:
    name = input("请输入用户名：")
    password = input("请输入密码：")
    if name=="root" and password=="admin":
        print("登录成功")
        break
    elif name=="root"and password!="admin":
        print("输入密码错误")
        count = count - 1
    if count==0:
        print("已锁定")
        break

count = 1
sum = 1
while True:
    count = count + 1
    sum = sum + count
    if count==100:
        break
print("1~100的数和为：",sum)

deep = 20
skip = 3
slide = 2
day = 0
while 1:
    deep -= skip
    if deep < 0:
        break
    deep += slide
    day += 1
print("天数:",day)

import random
num = random.randint(0,100)
count = 0
gold = 5000
while True:
    gold = gold - 1
    count = count + 1
    a = input("请输入你要猜的数：")
    a = int(a)
    if a > num:
        print("大了！")
    elif a < num:
        print("小了!")
    else:
        print("恭喜你","你本次输入了",count,"次")
    if count <= 3 and a == num:
        print("奖励200")
        break
    if gold <= 0:
        print("金币耗完")
        break
