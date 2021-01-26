# Author Chaudhary Hamdan

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    dic = {}
    ans = 0
    for i in range(n):
        arr[i] = int(arr[i])
        dic[arr[i]] = i
    for i in range(1,n+1):
        if i > 1:
            ans += abs(dic[i]-dic[i-1])
        else:
            ans += dic[i]
    print(ans)
    
  