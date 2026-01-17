
import random



class Cat :

    def __init__(self,name,atk,hp):
        self.name = name 
        self.hp = hp
        self.atk = atk
        print("喵喵叫")
    
    def scratch(self,enemy):

        luck = random.randint(1,100)

        if luck <= 20 :
            print(f"💨 {self.name} 抓了了个空！没有咬中！(Miss)")
        elif luck >= 80 :
            dmg = self.atk * 2
            enemy.hp -= dmg
            print(f"💥 暴击！！！{self.name} 狠狠抓了 {enemy.name} 一口，造成 {dmg} 点巨额伤害！狗还剩 {enemy.hp} HP")
        else :
            enemy.hp -= self.atk
            print(f"{self.name}抓了{enemy.name},造成了{self.atk}点伤害！狗还剩{enemy.hp}HP") 
        

class Dog :
    
    def __init__(self,name,atk,hp):
        self.name = name 
        self.atk = atk 
        self.hp = hp 
    
    def bite(self,enemy):

        luck = random.randint(1,100)

        if luck <= 20 :
            print(f"💨 {self.name} 扑了个空！没有咬中！(Miss)")
        elif luck >= 80 :
            dmg = self.atk * 2
            enemy.hp -= dmg
            print(f"💥 暴击！！！{self.name} 狠狠咬了 {enemy.name} 一口，造成 {dmg} 点巨额伤害！猫还剩 {enemy.hp} HP")
        else :
            enemy.hp -= self.atk
            print(f"{self.name}抓了{enemy.name},造成了{self.atk}点伤害！猫还剩{enemy.hp}HP") 

cat = Cat("耄耋",15,100)
dog = Dog("大狗叫",20,100)

while True:
    dog.bite(cat)
    
    if cat.hp <= 0 :
        print(f"大狗叫获得了胜利，耄耋倒下了")
        break
    cat.scratch(dog)
    if dog.hp <= 0 :
        print(f"耄耋获得了胜利，大狗叫倒下了")
        break
    print("-" * 30)
