
class Dog:

    def __init__(self,name,color):
        self.name = name
        self.color = color 
        print(f"！一只叫{self.name}的{self.color}的小狗诞生了")

    def bark(self):
        print(f"{self.name}: 汪汪汪！我是{self.color}的！")
    def eat(self, food):
        print(f"{self.name} 正在大口吃 {food}...")    

dog1 = Dog("旺财","黄色")
dog2 = Dog("来福","黑色")

print("-" * 20)

dog1.bark()
dog2.bark()

dog1.eat("肉骨头")