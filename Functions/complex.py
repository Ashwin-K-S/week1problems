def sum(a,b):
    if type(a) == type(b):
        return a + b


def main():
    try:
        x=int(input("Enter no1: "))
        y=int(input("Enter no2: "))
        total = sum(x,y)
        print(total)
    except ValueError:
        print("Error: The values passed are not of same datatpye")

main()
