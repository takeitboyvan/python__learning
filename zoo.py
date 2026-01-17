
class Monster :
    
    def attack(self):
        print("👿 怪物准备攻击...")
    
class Slim(Monster):
    def attack(self):
        super().attack()
        print("💧 史莱姆软绵绵地撞了你一下，扣了 5 滴血。")
    pass

class Dragon(Monster):
    def attack(self):
        super().attack()
        print("🔥 恶龙喷出了烈焰！你变成了烤肉！扣了 100 滴血！")
    pass

s1 = Slim()
s2 = Dragon()

cage = [s1,s2]

print("--- 动物园暴动 ---")

for Monster in cage :
    Monster.attack()
    pass
