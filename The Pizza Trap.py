

class pizza:
    
    def __init__(self,diameter,price):
        self.diameter = diameter
        self.price = price
        self.area = None

    def get_area(self):
        area = 3.14 * ((self.diameter/2)**2)
        self.area = area
        print(f"表面积为{area}")
        return area
    
    def get_unit_price(self):
        true_price = self.price/self.area
        print(f"每平方英寸{true_price}钱")


pizza1 = pizza(12,100)
pizza2 = pizza(6,40)

print("---大披萨数据---")
are_big = pizza1.get_area()
pizza1.get_unit_price()

print("\n---小披萨数据---")
are_small = pizza2.get_area()
pizza2.get_unit_price()

print("\n--- 最终结论 ---")
total_pizza2_area = are_small * 2

print(f"1个12寸面积: {are_big:.2f}")
print(f"2个6寸总面积: {total_pizza2_area:.2f}")

if are_big > total_pizza2_area:
    print("😱 结论：店员在忽悠你！1个12寸比2个6寸大多了！")
else:
    print("结论：店员是对的。")



