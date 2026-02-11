#Concept used:
# last_digit = num % 10
# remove_digit = num // 10

num = int(input("Num = "))
sign = -1 if num<0 else 1

num = abs(num)

if num == 0:
    print(num)

rev = 0
while num>0:
    last_digit = num % 10
    rev = rev*10 + last_digit
    num = num // 10

print(sign*rev)