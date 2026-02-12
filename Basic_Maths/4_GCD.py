#BRUTE FORCE
n1 = int(input("Num1 = "))
n2 = int(input("Num2 = "))

gcd = 1
for i in range (2, min(n1,n2)+1):
    if n1%i == 0 and n2%i == 0:
        gcd = i

print(gcd)


#Better Version
n1 = int(input("Num1 = "))
n2 = int(input("Num2 = "))

gcd = 1

for i in range(min(n1,n2),1,-1):
    if n1%i == 0 and n2%i == 0:
        gcd = i
        break

print(gcd)


#Euclidean Algorithm
#Cond: n1>n2
#TC: O(min(n1,n2)) and SC : O(1)

n1 = int(input("Num1 = "))
n2 = int(input("Num2 = "))

while n2 != 0:
    n1 , n2 = n2 , n1%n2

print(n1)





















