def nthXorFib(n, a, b): 
    if n == 0 :  
        return a  
    if n == 1 :  
        return b  
    if n == 2 :  
        return a ^ b  

    return nthXorFib(n % 3, a, b)  

t = int(input())
for _ in range(t):
    a,b,n = [int(x) for x in input().split()]
    print(nthXorFib(n, a, b))  

  
