shop = [
    ["lenovo thinkpad e580",5000],  # 0
    ["ipad 2021",3000],   # 1
    ["华为手表",3000], #
    ["辣条",3.5],
    ["大米",50],
    ["旺财QQ糖",50]
]

# 2.初始化自己的薪资
salary = input("请输入您的薪资：")
salary = int(salary)
A = 0       #余额

#抽取优惠券
import random
meter = 0

pa = random.randint(0,4)
if pa == 1:
    print("恭喜抽中辣条优惠券，满600减300")
    y = 1       #优惠券数量
else:
    print("恭喜抽中Lenovo电脑优惠券，半折甩卖")
    y = 2

# 我的购物车
mycart = []

while True:
    # 3.展示商品
    for index,value in enumerate(shop): #enumerate()枚举：将所有的可能都列举出来
        print(index,"  ",value)

    # 4.输入要买的编号:num 是商品编号
    num = input("请输入您要买的商品编号：")

    # 若是 0 1 2 3 4 5 6 7 8 9 ，  若是  Q或者q  ,  输入非法
    if num.isdigit():
        num = int(num) # 转换成数字
        # 判断是否有这个商品
        if num >= len(shop):  # 不存在
            print("商品不存在！！！请重新输入！！！")
        else:
            # 可以买东西
            if salary >= shop[num][1]:  # 某个商品的价格:正常买
                # 添加到购物车
                mycart.append(shop[num])  # 添加购物车
                A = salary - shop[num][1]  # 减去金额
                i = 0       #购买辣条数量
                j = 0       #购买lenovo数量
                while i < len(mycart):
                    if mycart[i][0] == "辣条" and y == 1:
                        lt = lt + mycart[i][1]
                        if lt == 600:
                            A = A + 300
                            print("您成功的使用了辣条优惠券，余额为",salary,"元")
                            y = 0
                            break
                    elif i < len(mycart) - 1:
                        i = i + 1
                    else:
                        break
                while j < len(mycart):
                    if mycart[j][0] == "lenovo thinkpad e580" and y == 2:
                        A = A + mycart[j][1]/2
                        print("您成功的使用了lenovo优惠券，余额为", salary, "元")
                        y = 0
                        break
                    elif j < len(mycart) - 1:
                        j = j +1
                    else:
                        break
                print("成功添加到购物车！！！余额为：",salary)
            else:
                print("对不起，穷鬼，您的金额不足！！！！！")
    elif num == "Q" or num == "q":
        print("------------欢迎下次光临！！！！----------")

        break
    else:
        print("输入非法！！！！请重新输入！！！")

# 打印购物小条：
print("您本次购物商品如下：")
for index,value in enumerate(mycart):
    print(index,"  ",value)
print("您的余额为：",A,"本次购物获得积分为",(salary - A)/10)