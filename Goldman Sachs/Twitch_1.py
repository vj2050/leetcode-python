def func(A,T):
    s = set()
    for i in A:
        if T[i] not in A:
            s.add((T[i]))
    print("set ", s)
    i = 0
    li = list(s)
    print("li ", li)
    while(i<len(li)):

        if T[li[i]] not in li:
            li.append(T[li[i]])
        i+=1
    for i in A:
        if i not in li:
            li.append(i)
    return len(li)
print(func([0,1],[1,0]))