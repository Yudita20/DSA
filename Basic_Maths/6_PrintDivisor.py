import math
n = int(input("Num = "))

res = []
r = int(math.sqrt(n))
for i in range(1 , r+1):
    if n%i == 0:
        res.append(i)
        if i != n//i:
            res.append(n//i)

print(res)
