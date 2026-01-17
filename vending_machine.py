
def get_price(choice):
    if choice == "1":
        return 2
    elif choice == "2":
        return 5
    elif choice == "3":
        return 10
    else:
        return 0

    
balance = int(input("请输入你的余额"))

while True:
    print(f"当前余额: {balance}")
    choice = input("请选择(1/2/3/q): ")

    if choice == "q":
        # ... 退钱，走人 ...
        break
    
    # 1. 先问函数，这个东西多少钱
    price = get_price(choice)

    # 2. 检查是不是瞎输入的
    if price == 0:
        print("没有这个商品！")
        continue # 跳过本次循环，重新开始

    # 3. 检查钱够不够
    if balance >= price:
        balance -= price
        if choice == "1" :
            name = ("水")
            money = 2
        elif choice == "2":
            name = ("可乐")
            money = 5
        else :
            name = ("能量饮料")
            money = 10
        
        print(f"购买{name}成功,花费了{money}")
        # ... 扣钱，出货 ...
    else:
        print("余额不足！")