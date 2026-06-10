def myAtoi(s):
    sign = 1
    res = ""

    i = 0
    # Checking for leading space
    while i < len(s) and s[i] == " ":
        i += 1

    if i == len(s):
        return 0

    # Checking for sign
    if s[i] == "-":
        sign = -1
        i += 1
    elif s[i] == "+":
        sign = 1
        i += 1
    else:
        sign = 1

    # Checking for leading zeroes
    while i < len(s) and s[i] == '0':
        i += 1

    # Digits checking
    while i < len(s) and s[i].isdigit():
        res += s[i]
        i += 1

    if res == "":
        return 0

    num = sign * int(res)

    if num > 2147483647:
        return 2147483647
    elif num < -2147483648:
        return -2147483648
    else:
        return num

str_s = "         -0004624abc"
print(myAtoi(str_s))

