def largest_odd(s):
    max_odd = float("-inf")
    for i in range(len(s)):
        for j in range(i , len(s)):
            if int(s[i:j+1]) % 2 != 0:
                max_odd = max(max_odd , int(s[i:j+1]))

    return max_odd

def largest_odd_number(s):
    i = len(s)-1
    while i >= 0:
        if int(s[i]) % 2 != 0:
            break
        i -= 1

    j = 0
    while j <= i and s[j] == "0":
        j += 1

    return s[j:i+1]

org_str = "004"
print(largest_odd_number(org_str))


# print(largest_odd(org_str))
