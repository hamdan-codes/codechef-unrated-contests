# Author Chaudhary Hamdan

a = input()
b = input()

al,bl = len(a), len(b)
present = 0
for i in range(al-1,-1,-1):
    x = a[i:]
    if x not in b:
        present = i+1
        break
a = a[present:]
al = len(a)
if a+'y' in b:
    print("YES")
else:
    print("NO")


