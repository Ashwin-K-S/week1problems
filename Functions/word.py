def add(var):
    list.append(var)
    return list

list= []
n = int(input("Enter the no. of words: "))
for i in range(n):
    word = input("Enter word: ")
    list = add(word)
print(list)
