# Author Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n = int(input())
    a = input().split()
    ans = 0
    got = 0
    cur = 1
    siz = 0
    for i in range(n):
        x = int(a[i])
        if x != cur:
            if siz > ans:
                ans = siz
            siz = 0
            cur = 1
            
        else:
            cur += 1
            siz += 1
        
    print(max(siz,ans))
            
    
    


