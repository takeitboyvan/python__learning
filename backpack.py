
def update_backpack(currnet_bag,action,item):
    if action == "1":
        if len(currnet_bag) >= 5:
            print ("背包满了装不下")
        else:
            currnet_bag.append(item)
            print(f"捡起了物品{item}")
    if action == "2":
        if item in currnet_bag:
            currnet_bag.remove(item)
            print(f"你丢弃了{item}")
        else:
            print("背包里没有这个东西！")
    return currnet_bag

my_bag = []

while True:
    print(f"你背包当前的状态{my_bag}")
    act = input("输入操作：1.捡 / 2.扔 / q.退出")

    if act == "q" :
        print("退出背包")
        break
    if act not in ["1","2"]:
        print("请输入正确的选项！")
        continue
    if act == "1" :
        g_item = input("输入你要拾取的物品")
    if act == "2" :
        g_item = input("输入你要丢掉的物品") 
    my_bag = update_backpack(my_bag,act,g_item)
    


