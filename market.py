
def calc_price(total_money,is_vip) :
    if total_money < 100 :
        if total_money < 0 :
            total_money = 0
    elif total_money <300 :
        total_money = total_money*0.9 
    else: 
        total_money = total_money*0.8
    
    if is_vip == True :
        total_money -= 20
    if total_money < 0 : 
        total_money = 0 
    return total_money



amount = float(input("请输入金额"))
vip = input("是否VIP？")

if vip == "y":
    vip_bool = True
else :
    vip_bool = False

finally_amount = calc_price(amount,vip_bool)
print(f"您原价{amount},打折后最终只需要支付{finally_amount}")
