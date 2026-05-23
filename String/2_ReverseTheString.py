def reverse_string(s):
    new_str = s.split()
    result = ""

    for i in range(len(new_str)-1 , -1 , -1):
        result += new_str[i]
        if i != 0:
            result += " "

    return result

# def reverse(s):
#     result = ""
#     i = j = len(s)-1
#     while j >= 0:
#         while s[j] == " " and j >= 0:
#             j -= 1
#
#         if j < 0:
#             break
#
#         i = j
#         while j >= 0 and s[j] != " ":
#             j -= 1
#
#         result += s[j + 1: i + 1]
#         if j > 0:
#             result += " "
#
#     return result

org_str = "  hello world  "
# print(reverse(org_str))
print(reverse_string(org_str))