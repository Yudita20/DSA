def isArmstrong(num):
    n1 = num
    count = len(str(num))
    s = 0
    while num>0:
        last_digit = num % 10
        s = s + (last_digit ** count)
        num = num // 10

    if n1 == s:
        return True
    else:
        return False

n = int(input("Num = "))
print(isArmstrong(n))
