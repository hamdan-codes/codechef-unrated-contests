t = int(input())
for _ in range(t):
    n,m = [int(x) for x in input().split()]
    a = []
    for i in range(n):
        a.append(input())
    s = input()
    l = len(s)
    flag = 0
    for i in range(l):
        if(s[i] in a[i%n]):
            f = a[i%n].index(s[i])
            a[i%n] = a[i%n][:f]+a[i%n][f+1:]
        else:
            flag = 1
            break
    if flag == 0:
        print('Yes')
    else:
        print('No')
    
    


