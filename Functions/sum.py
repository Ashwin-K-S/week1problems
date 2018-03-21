def sum(list):
    sum=0
    for i in range(len(list)):
        sum = sum + list[i]
    return sum

def main():
    alist = []
    total = 0
    n = int(input("Enter the size: "))
    for i in range(n):
        num = int(input("Enter the num: "))
        alist.append(num)
        total = sum(alist)
    print(total)

main()
