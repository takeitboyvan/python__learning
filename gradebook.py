
def update_grade(grade_dict,subject,score):
    if 0 <= score <= 100 :
        grade_dict[subject] = score 
        print(f"{subject}成绩已经更新为{score}")
    else :
        print("分数无效！请输入正确的分数！")
    return grade_dict

def calc_average(grade_dict):
    if len(grade_dict) == 0 :
        return 0
    all_grade = sum(grade_dict.values())
    finally_avg = all_grade/len(grade_dict) 
    return finally_avg

my_grades = {}

while True:
    print("-" * 20)
    print(f"当前的班级成绩单{my_grades}")
    act = input("请输入：1.录入成绩 / 2.计算平均分 / q.退出。")

    if act == "q":
        print("正在退出")
        break
    if act == "1":
        subject = input("输入科目名字")
        score = int(input("请输入分数"))
        my_grades = update_grade(my_grades,subject,score)

    elif act == "2":
        avg = calc_average(my_grades)   
        print(f" 当前平均分是{avg}")
    else:
        print("请输入正确的选项！")


