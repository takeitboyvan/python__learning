
import random

class Weapon :

    def __init__(self,name,atk_bonus,price):
        self.name = name 
        self.atk_bonus = atk_bonus 
        self.price = price
        print(f"武器:{name},攻击力{atk_bonus},价值{price}")

class Hero :

    def __init__(self,name,gold):
        self.name = name
        self.gold = gold
        self.weapon = None

    def buy_weapon(self,weapon):
        if self.gold >= weapon.price:
            self.gold -= weapon.price 
            self.weapon = weapon 
            print(f"购买成功！装备了{blade.name}")
        else :
            print(f"你的钱不足！请赚取更多金币！")    

    def attack(self):
        if self.weapon is None :
            print("赤手空拳打了 10 点伤害")    
        else :
            total_dmg = 10 + self.weapon.atk_bonus
            print(f"用{self.weapon.name}打出了{total_dmg}点伤害")

blade = Weapon("屠龙刀", 999, 500)
stick = Weapon("小木棍", 5, 10)

player = Hero("亚瑟", 1000)

player.attack()           # 没武器时
player.buy_weapon(blade)  # 买刀
player.attack()           # 有武器时