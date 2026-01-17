

class Cat :

    def __init__(self,name,hp):
        self.name = name 
        self.hp = hp
        print("喵喵叫")

class Dog :
    
    def __init__(self,name,atk):
        self.name = name 
        self.atk = atk 
    
    def bite(self,enemy):
        enemy.hp -= self.atk
        print(f"{self.name}咬了{enemy.name},造成了{self.atk}点伤害！猫还剩{enemy.hp}HP") 

cat = Cat("耄耋",100)
dog = Dog("大狗叫",20)

while True:
    if cat.hp > 0 :
        dog.bite(cat)
    else :
        print(f"系统提示：{cat.name} 已经倒下了！{dog.name} 获胜！")
        break


