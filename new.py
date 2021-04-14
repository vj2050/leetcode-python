def outsiderfunc():
    li = []
    unique = []
    inputstr = ''
    while inputstr != 'stop':
        inputstr = str(input())
        if inputstr == 'stop':
            break
        li.append(inputstr)
    for i in li:
        if li.count(i) == 1:
            unique.append(i)

    if len(unique) != 0:
        return "the outsider is :" + str(unique)[1:-1]
    else:
        return "There is no outsider"


print(outsiderfunc())
