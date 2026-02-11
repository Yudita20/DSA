num = int(input("Num = "))
n = num
sign = -1 if num<0 else 1

num = abs(num)

if num == 0:
    print(num)

rev = 0
while num>0:
    last_digit = num % 10
    rev = rev*10 + last_digit
    num = num // 10

rev = sign * rev
if n == rev:
    print("yes")
else:
    print("no")