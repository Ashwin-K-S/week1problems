def srch(list,key):
    pos = 0
    flag = 0
    for i in range(len(list)):
        if list[i] == key:
            flag=1
            pos = i


    if flag == 1:
        print("Key found at : ",pos)
    else:
        print("Key not found")

list = ["Hello", 1, 1.234, "My_World"]
srch(list,1)
