INT_MIN = -2**31
INT_MAX = 2**31-1

def stringToInt(s):
    n = len(s)
    i = 0

    while i < n  and s[i] == " ":
        i += 1

    sign = 1
    if i < n and (s[i] == "+" or s[i] == "-"):
        sign = 1 if s[i] == "+" else -1
        i += 1

    return helperFunction(s,i,0,sign)

def helperFunction(s, i, num, sign):
    if i >= len(s) or not s[i].isdigit():
        return sign*num


    num = num*10 + int(s[i])

    if sign * num <= INT_MIN: return INT_MAX
    if sign * num >= INT_MAX: return INT_MAX

    return helperFunction(s, i+1 , num, sign)


if __name__ == "__main__":
    s = "000-42"
    print(stringToInt(s))






