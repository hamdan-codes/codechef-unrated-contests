# Author Chaudhary Hamdan

t = int(input())
for _ in range(t):
    r = int(input())
    n = int(input())
    a = input().split()
    for i in range(n):
        if int(a[i]) >= r:
            print(i+1)
            break
