
def get_price(choice):
    # 【修复】这里全部改成字符串 "1", "2", "3"
    if choice == "1":
        return 2 
    elif choice == "2":
        return 5
    elif choice == "3":
        return 10
    else:
        return 0

# 为了方便，我顺手帮你加了个取名字的函数
# 这样主程序就不用写一堆 if/else 了
def get_name(choice):
    if choice == "1": return "矿泉水"
    elif choice == "2": return "可乐"
    elif choice == "3": return "能量饮料"
    else: return "未知商品"

# --- 主程序 ---
balance = int(input("请输入你的余额: "))

while True:
    print(f"💰 当前余额: {balance}")
    print("菜单: 1.水(2元) / 2.可乐(5元) / 3.能量饮料(10元) / q.退出")
    choice = input("请选择: ")

    if choice == "q":
        print(f"👋 已退回余额 {balance} 元，欢迎下次光临！")
        break
    
    # 1. 问价格
    price = get_price(choice)

    # 2. 检查有没有这个商品
    if price == 0:
        print("❌ 没有这个商品！")
        continue 

    # 3. 检查钱够不够
    if balance >= price:
        balance -= price
        
        # 【优化】不用再手动写 money = 2 了，直接用 price
        # 【优化】调用上面的新函数获取名字
        product_name = get_name(choice)
        
        print(f"✅ 购买 {product_name} 成功, 花费了 {price} 元")
    else:
        print("💸 余额不足！")
    
    print("-" * 20) # 画条分割线好看点