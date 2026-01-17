
def update_balance(current,action,amount):
    if action == "1" :
        current += amount
        print("✅ 存钱成功！")
    elif action == "2" :
        if amount > current :
            print("❌ 余额不足，取钱失败！")
        else :
            current -= amount
            print("✅ 取钱成功！")
    return current

my_money = 0 

while True :
    print("-" * 20)
    print(f"您当前的余额{my_money}")
    act = input("1.存钱 / 2.取钱 / q.退出。")

    if act == "q":
        print(f"已退出银行，您的余额为{my_money}")
        break
    if act not in ["1", "2"]:
        print("⚠️ 输入错误，请输入 1, 2 或 q")
        continue # 跳过这一轮，重新开始
    if act == "1":
        amount = int(input("请输入你要存多少钱"))
    elif act == "2":
        amount = int(input("请输入你要取多少钱"))
    my_money = update_balance(my_money, act, amount)    

