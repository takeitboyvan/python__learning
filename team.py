
class Monster:
    def __init__(self, name , atk):
        self.name = name
        self.atk = atk
    
    def attack(self):
        print(f"👿 {self.name} 发起普通攻击！")

class Slime(Monster):
    def attack(self):
        print(f"💧 {self.name} 吐出了酸液！")

class Dragon(Monster):
    def attack(self):
        print(f"🔥 {self.name} 喷射龙息！")

class Team:
    def __init__(self):
        members = [ ]
        self.members = members

    def add_member(self,monster):
        self.members.append(monster)
        print(f"✅ {monster.name} 加入了队伍！")
    
    def start_battle(self):
        print("\n⚔️ --- 全军突击 --- ⚔️")
        total_dmg = 0 


        for m in self.members:
            total_dmg = total_dmg + m.atk
            m.attack()
        print(f"☠️ 本轮总伤害：{total_dmg} 点！")

my_team = Team()

s1 = Slime("绿史莱姆",10)
d1 = Dragon("红龙",100)
s2 = Slime("蓝史莱姆",10)


my_team.add_member(s1)
my_team.add_member(d1)
my_team.add_member(s2)

my_team.start_battle()

