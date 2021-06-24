import random

num = random.randint(0,101)
count = 0
coin = 5000

while True:
    count = count + 1
    coin = coin - 100
    num1 = input("请输入您想要输入的数字：")
    num1 = int(num1)
    if count <= 7:
        if num1 < num:
            print("您输入的数字小了")
        elif num1 > num:
            print("您输入的数字大了")
        else:
            coin = coin + 5000
            print("恭喜您！您抽中中奖数字：", num, "您一共抽取了：", count, "次", "获得5000奖金，您现在还有", coin, "个金币")
            break
    else:
        print("您已经猜了7次，不能继续游戏了，请重新开始")
        break

