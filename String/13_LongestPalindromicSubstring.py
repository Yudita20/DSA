def palindrome_string(s , i ,j):
    if i >= j:
        return True

    if s[i] == s[j]:
        return palindrome_string(s , i+1 , j-1)
    else:
        return False

def longest_palindromic_string(s):
    max_len = 0
    starting = -1

    for i in range(len(s)):
        for j in range(i , len(s)):
            if palindrome_string(s , i , j):
                if j-i+1 > max_len:
                    max_len = j-i+1
                    starting = i

    return s[starting:max_len+starting]


def expand_centre(s , left  ,right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left+1 : right]

def palindromic(s):
    if len(s) <= 1:
        return s

    max_str = s[0]

    for i in range(len(s)):
        #odd and even
        odd = expand_centre(s , i , i)
        even = expand_centre(s , i , i+1)

        if len(odd) > len(max_str):
            max_str = odd
        if len(even) > len(max_str):
            max_str = even

    return max_str

str_s = "c"
print(palindromic(str_s))
# T(n) = O(n^2)
# S(n) = O(1)
print(longest_palindromic_string(str_s))
# T(n) = O(n^3)
# S(n) = O(max_len)