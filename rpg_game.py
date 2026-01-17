
import random

# --- 1. 武器类 (已完成) ---
class Weapon:
    def __init__(self, name, atk, price):
        self.name = name
        self.atk = atk
        self.price = price

# --- 2. 怪物类 (已完成) ---
class Monster:
    def __init__(self, name, hp, atk, gold_reward):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.gold_reward = gold_reward

# --- 3. 英雄类 (核心挑战！) ---
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100       # 初始血量
        self.gold = 0       # 初始没钱
        self.weapon = None  # 初始没武器(空枪套)

    # 治疗功能
    def heal(self):
        self.hp = 100
        print("✨ 血量已回满！")

    # 购买武器 (把你刚才学会的逻辑写在这里)
    def buy_weapon(self, weapon):
        if self.gold >= weapon.price:
            self.gold -= weapon.price
            # ### 填空 1：把武器对象装进枪套 ###
            self.weapon = weapon# __________________________
            print(f"✅ 购买成功！装备了 {self.weapon.name} (攻击力+{self.weapon.atk})")
        else:
            print("❌ 金币不足！")

    # 攻击怪物 (对象交互！)
    def attack(self, enemy):
        # 基础伤害 10
        dmg = 10

        if self.weapon is not None :
            dmg = dmg + self.weapon.atk
        
        enemy.hp -= dmg
        
        
        # ### 填空 2：如果手里有武器，把武器攻击力加到 dmg 上 ###
        # if _____________________:
        #     dmg = dmg + _________________
        
        # ### 填空 3：扣怪物的血 ###
        # ______________________
        
        print(f"⚔️ 你攻击了 {enemy.name}，造成了 {dmg} 点伤害！")

# --- 4. 游戏主程序 ---

player = Hero("勇者")

# 武器商店清单
shop_weapons = [
    Weapon("铁剑", 10, 50),
    Weapon("屠龙刀", 100, 200)
]

print("🏰 欢迎来到无尽地牢！")

while True:
    print("-" * 30)
    print(f"👤 状态: HP={player.hp} | 金币=${player.gold}")
    if player.weapon:
        print(f"🗡️ 武器: {player.weapon.name}")
    else:
        print("👊 武器: 无")
    
    cmd = input("\n你要做什么？(1.探索打怪 / 2.回城买武器 / 3.回血 / q.退出): ")

    if cmd == "q":
        break

    elif cmd == "3":
        player.heal()

    elif cmd == "2":
        print("\n=== 武器商店 ===")
        # 遍历展示武器
        for i, w in enumerate(shop_weapons):
            print(f"{i}. {w.name} (攻+{w.atk}) - 价格${w.price}")
        
        choice = input("输入序号购买 (不管我就回去了): ")
        if choice in ["0", "1"]:
            target_weapon = shop_weapons[int(choice)]
            player.buy_weapon(target_weapon)
            # ### 填空 4：从列表里拿出武器对象，传给 buy_weapon ###
            # target_weapon = shop_weapons[_______]
            # player.buy_weapon(__________)

    elif cmd == "1":
        # 随机生成一个怪物
        m_hp = random.randint(30, 80)
        m_gold = random.randint(20, 100)
        monster = Monster("史莱姆", m_hp, 10, m_gold)
        
        print(f"\n👿 遭遇了 {monster.name} (HP={monster.hp})！战斗开始！")
        
        # 战斗循环
        while monster.hp > 0 and player.hp > 0:
            # 玩家打怪
            player.attack(monster)
            
            if monster.hp <= 0:
                print(f"🎉 胜利！获得了 {monster.gold_reward} 金币！")
                player.gold += monster.gold_reward
                break
                
            # 怪打玩家
            dmg = monster.atk
            player.hp -= dmg
            print(f"🩸 怪物反击！你受到了 {dmg} 点伤害！")
            
            if player.hp <= 0:
                print("💀 你挂了... 游戏结束。")
                exit() # 直接结束程序