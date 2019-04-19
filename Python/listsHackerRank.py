if __name__ == '__main__':
    N = int(input())

    inputs = [input().split() for _ in range(N)]
    my_list = []
    for i in inputs:
        if i[0] == 'insert':
            my_list.insert(int(i[1]),int(i[2]))
        elif i[0] == 'print':
            print(my_list)
        elif i[0] == 'remove':
            my_list.remove(int(i[1]))
        elif i[0] == 'append':
            my_list.append(int(i[1]))     
        elif i[0] == 'sort':
            my_list.sort()
        elif i[0] == 'pop':
            my_list.pop()
        elif i[0] == 'reverse':
            my_list.reverse()