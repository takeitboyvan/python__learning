
def borrow_book(lib_dict,book_name):
    if book_name in lib_dict:
        if lib_dict[book_name] > 0:
            lib_dict[book_name] -= 1
            print(f"成功借出{book_name},剩余库存{lib_dict[book_name]}")
        else:
            print(f"没库存了！{book_name}已经被借完了")
    else :
        print("我们没有这本书！")
    return lib_dict        
 

def return_book(lib_dict,book_name):
    if book_name not in lib_dict:
        print("这不是我们的书，拒收！")
    else :
        lib_dict[book_name] += 1
        print(f"归还{book_name}成功，")
    return lib_dict
 
my_books = {
    "python编程":5,
    "哈利波特":3,
    "三体":0
}

while True:
    print(f"当前的藏书数量{my_books}")
    act = input("请输入操作：1.借书 / 2.还书 / q.退出")

    if act == "q":
        print("退出图书系统")
        break
    if act == "1" :
        book_name = input("请输入书名")
        my_books = borrow_book(my_books,book_name)
    if act == "2" :
        book_name = input("请输入书名")
        my_books = return_book(my_books,book_name)
