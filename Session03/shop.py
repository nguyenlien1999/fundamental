items=["T-shirt","Sweater"]
while True:
    manipulation=str(input("Welcom to our shop, what do you want (C,R,U,D)  "))

    if manipulation=="R":
        print("our items",end="")
        print(items[i])
    elif manipulation=="C":
        items.append(input("Enter new item:"))
    elif manipulation=="U":
        new_item=str(input("New item : "))
        items[new_item-1]=input("Update: ")
    elif manipulation=="D":
        new_item=str(input("Delete"))
        del items[3]
    else:
        print("chương trình cho phép bạn 4 thao tác:Create, Read, Update, Delete, hiện chưa có thao tác nào ngoài chúng")
    print("Our items:",items)




        



