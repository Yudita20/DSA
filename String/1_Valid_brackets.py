def valid_parentheses(s):
    b = 0
    res_str = ""

    for ch in s:
        if ch == "(":
            if b > 0:
                res_str += ch
            b += 1
        else:
            b -= 1
            if b > 0:
                res_str += ch
    return res_str

org_str = "()(()())(())"
print(valid_parentheses(org_str))