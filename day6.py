import random
shop = [
    ["Lenovo phone",12000],
    ["小米彩电",6000],
    ["美的空调",5000],
    ["iPhone 12",2000],
    ["卫龙辣条",5],
    ["冰淇凌",7.5]
]

for index,value in enumerate(shop) :
    print(index,"",value)
salary = int(input("请输入您的钱包余额："))
flag = random.randint(1,8)
if flag >= 1 and flag <= 3 :
    print("获得了一张联想5折卷")
else:
    print("获得了一张苹果6折卷")
mycar = []
while True :
    for index,value in enumerate(shop) :
        print(index,"",value)
    num = input("请输入商品编号：")
    if num.isdigit() :
        num = int(num)
        if num > len(shop) :
            print("输入的商品编号不存在，请重新输入！")
        elif num == 0 and (flag >= 1 and flag <= 3) :
            if salary >= shop[num][1] * 0.5 :
                mycar.append(shop[num])
                salary = salary - shop[num][1] * 0.5
                print("购买成功，您的余额还有：",salary,"元!")
            else :
                print("您的余额不足，购买失败！")
        elif num ==3 and (flag > 3 and flag <= 7) :
            if salary >= shop[num][1] * 0.6 :
                mycar.append(shop[num])
                salary = salary - shop[num][1] * 0.6
                print("购买成功，您的余额还有：",salary,"元!")
            else :
                print("您的余额不足，购买失败！")
        else :
            if salary >= shop[num][1] :
                mycar.append(shop[num])
                salary = salary - shop[num][1]
                print("购买成功，您的余额还有：", salary, "元!")
            else:
                print("您的余额不足，购买失败！")
    elif num == 'q' or num == 'Q' :
        print("欢迎下次光临！")
        break
    else :
        print("输入非法！请重新输入！")

print("您本次的购物情况如下：")
for index,value in enumerate(mycar):
    print(index,"",value)
print("您的余额为：￥",salary)