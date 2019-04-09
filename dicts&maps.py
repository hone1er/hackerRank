# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
names = [(input().split()) for x in range(n)]
phonebook = {}
for name in names:
    phonebook[name[0]] = name[1]


while name != '':
    try:
        name = input()
        if name in phonebook:
            print(f"{name}={phonebook[name]}")
        else:
            print("Not found")
    except EOFError:
        break
        
