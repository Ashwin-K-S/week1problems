def filter(list):
    for i in range(len(list)):
        if list[i] % 2 != 0:
            del list[i]
    return list

def main():
    alist= []
    n = int(input("Enter the size: "))
    for i in range(n):
        num = int(input("Enter the num: "))
        alist.append(num)
        even = filter(alist)
    print(alist)

main()
