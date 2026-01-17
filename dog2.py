
class Dog:

    def __init__(self,name,color,age):
        self.name = name
        self.color = color 
        self.age = age
        print(f"！一只叫{self.name}的{self.color}的小狗诞生了")

    def bark(self):
        print(f"{self.name}: 汪汪汪！我是{self.color}的！")
    def eat(self, food):
        print(f"{self.name} 正在大口吃 {food}...") 
    def grow_up(self,increase=1) :
        self.age += increase
        print(f"{self.name}过生日了！居然一下长了 {increase} 岁！现在{self.age}岁了！")


dog1 = Dog("旺财","黄色",2)
dog2 = Dog("来福","黑色",3)

print("-" * 20)

dog1.grow_up(3)