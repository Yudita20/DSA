def max_depth_parenthesis(s):
    b = 0
    max_depth = b

    for ch in s:
        if ch == "(":
            b += 1
            max_depth = max(max_depth , b)
        elif ch == ")":
            b -= 1

    return max_depth

str_s = "()(())((()()))"
print(max_depth_parenthesis(str_s))