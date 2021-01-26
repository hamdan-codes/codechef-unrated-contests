# Author Chaudhary Hamdan

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


t = int(input())
for _ in range(t):
    n,k = [int(x) for x in input().split()]
    if k == 0:
        print(0)
        continue
    if n == 0:
        print(0)
        continue
    setbit = 1<<(k-1)
    c = 0
    fact = list(factors(n))
    for a in fact:
        if a & setbit:
            c += 1
    print(c)


