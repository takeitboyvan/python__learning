
import random

class Animal :

    def __init__(self,name,atk,hp,style):
        self.name = name 
        self.hp = hp
        self.atk = atk
        self.style = style
    
    def Attack(self,enemy):

        luck = random.randint(1,100)

        if luck <= 20 :
            print(f"💨 {self.name} 攻击了个空！没有咬中！(Miss)")
        elif luck >= 80 :
            dmg = self.atk * 2
            enemy.hp -= dmg
            print(f"💥 暴击！！！{self.name} 狠狠的{self.style}了 {enemy.name} ，造成 {dmg} 点巨额伤害！{enemy.name}还剩 {enemy.hp} HP")
        else :
            enemy.hp -= self.atk
            print(f"{self.name}狠狠的{self.style}了{enemy.name},造成了{self.atk}点伤害！{enemy.name}还剩{enemy.hp}HP") 
        

class Dog(Animal):
    pass

class Cat(Animal):
    pass

cat = Cat("耄耋",15,100,"抓")
dog = Dog("大狗叫",20,100,"咬")

while True:
    dog.Attack(cat)
    
    if cat.hp <= 0 :
        print(f"大狗叫获得了胜利，耄耋倒下了")
        break
    cat.Attack(dog)
    if dog.hp <= 0 :
        print(f"耄耋获得了胜利，大狗叫倒下了")
        break
    print("-" * 30)
