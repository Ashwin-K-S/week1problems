dict = {'a':"Hello",'b':"Hey", 3:"Hi"}
n = int(input("Enter no. of values to be entered: "))
for i in range(n):
    k = input("Enter key: ")
    v = input("Enter value: ")
    if k not in dict:
        dict[k] = v

print(dict)
