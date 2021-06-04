import random
# 银行的库
names = {}
'''
{
    "张三":{address:"沙河北大桥桥底下",money:546,account:1a5sdf1af},
    "张三":{address:"沙河北大桥桥底下",money:546}
}
'''

# 开户行名称
bank_name = "中国工商银行昌平支行"
# 欢迎页面的模板
welcome = '''
    -----------------------------------------
    -     欢迎来到中国工商银行账户管理系统     -
    -----------------------------------------
    -   1.开户                               -
    -   2.存钱                               -
    -   3.取钱                               -
    -   4.转账                               -
    -   5.查询                               -
    -   6.Bye!                               -
    ------------------------------------------
'''


def getRandom():
    li = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f"]
    string = ""
    for i in range(8):
        ch = li[random.randint(0,len(li) - 1)]
        string = string +  ch
    return string

# 银行的开户逻辑
def bank_addUser(account,username,password,money,country,province,street,door):
    # 1.判断是否已满
    if len(names)  >= 100:
        return 3
    # 2.判断是否存在:依据是用户名
    if username in names:
        return 2
    # 3.开户
    names[account] = {
        "account":account,
        "username":username,
        "password":password,
        "money":money,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name
    }
    return 1


# 开户操作
def addUser():
    username = input("请输入您的姓名：")
    password = input("请输入你的密码：")
    money = int(input("请输入您的账户余额：")) # "123"  123
    print("下面请输入您的个人地址信息：")
    country = input("请输入您的国籍：")
    province =  input("请输入您的省份：")
    street = input("请输入您的居住街道：")
    door = input("请输入您的门牌号：")
    account = getRandom()
    status = bank_addUser(account,username,password,money,country,province,street,door)
    if status == 1:
        print("恭喜开户成功！以下是您的个人信息：")
        info = '''
            ----------个人信息 【工商银行】--------
            用户名：%s,
            密码：%s,
            账号：%s,
            余额：%s,
            国家：%s,
            省份：%s,
            街道:%s,
            门牌号：%s
            开户行名称：%s
            ------------------------------------
        '''
        print(info % (username,password,account,money,country,province,street,door,bank_name))

    elif status == 2:
        print("对不起，您的账户已存在！请勿重复开户！")
    elif status == 3:
        print("对不起，用户库已满，请携带证件到其他银行办理！")
#存钱
def cunkuan():
    account = input("请输入您的帐号：")
    # 1判断是否存在
    if account in names:
        mima = input("请输入您的帐号密码：")
        #判断密码是否正确
        if mima == names.get(account).get("password"):
            jine = input("请输入您要存款的金额：")
            s = int(names.get(account).get("money"))
            jine = int(jine)
            s = s + jine
            print("存款操作成功,您当前的余额为：",s,"￥")
        else:
            print("输入密码错误！请重新输入！")
    else:
        print("没有此账号！")
#取钱
def bank_addTake(account,password,takemoney):
    if account in names:
        if password == names.get(account).get('password'):
            s = int(names[account]["money"])
            if takemoney > s:
                return 3
            else:
                return  4
        else:
            return 2
    else:
        return 1

def addTake():
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    takemoney = int(input("请输入您要取钱的金额"))
    status = bank_addTake(account,password,takemoney)
    if status ==1:
        print("输入账户名错误")
    elif status == 2:
        print("密码输入错误")
    elif status == 3:
        print("账户余额不足")
    elif status == 4:
        names[account]["money"] = names[account]["money"] - takemoney
        print("取钱成功")
        print("您的余额为：",names[account]["money"])

#转账操作
def transfer_money():
    account_out= input("请输入转出账号：")
    account_in = input("请输入转入账号：")
    password = input("请输入转出账号密码：")
    money = int(input("转出余额："))
    a = transfer_accounts(account_out,account_in,password,money)
    if a == 1:
        print("账号不对！")
    elif a==0:
        print("转账成功")
    elif a == 2:
        print("密码不对!")
    elif a == 3:
        print("钱不够!")
#转账逻辑
def transfer_accounts(account_out,account_in,password,money):
    if account_out not in names and account_in not in names:
        return 1
    if password not in names[account_out]["password"]:
        return 2
    if money > names[account_out]["money"]:
        return 3
    m_out = 0
    m_in = 0
    m_out = names[account_out]['money'] - money
    names[account_out]['money'] = m_out
    m_in = names[account_in]['money'] + money
    names[account_in]['money'] = m_in
    return 0
#查询
def bank_addinquiry(account,password,):
    if account in names:
        if password == names.get(account).get('password'):
            return 1
        else:
            return 2
    else:
        return 3

def addinquiry():
    account = input("请输入您的账户：")
    password = input("请输入你的密码：")
    status = bank_addinquiry(account,password,)
    if status == 1:
        info = '''
                    ----------个人信息 【工商银行】--------
                    用户名：%s,
                    密码：%s,
                    账号：%s,
                    余额：%s,
                    国家：%s,
                    省份：%s,
                    街道:%s,
                    门牌号：%s
                    开户行名称：%s
                    ------------------------------------
                '''
        print(info % (names.get(account).get('username'), names.get(account).get('password'), names.get(account).get('account'), names.get(account).get('money'),
                      names.get(account).get('country'), names.get(account).get('province'), names.get(account).get('street'), names.get(account).get('door'),
                      names.get(account).get('bank_name')))
    elif status == 2:
        print("密码输入错误")
    elif status == 3:
        print("账户输入错误")

# 入口程序
while True:
    print(welcome)
    chose = input("请输入您的业务编号：")
    if chose == '1':
        addUser()
    elif chose == '2':
        cunkuan()
    elif chose == '3':
        addTake()
    elif chose == '4':
        transfer_money()
    elif chose == '5':
        addinquiry()
    elif chose == '6':
        break
    else:
        print("输入非法！别瞎弄！")