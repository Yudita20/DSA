def roman_integer(s):
    roman_map = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    roman_sum = roman_map[s[len(s)-1]]
    for i in range(len(s)-2 , -1 , -1):
        if roman_map[s[i+1]] > roman_map[s[i]]:
            roman_sum -= roman_map[s[i]]
        else:
            roman_sum += roman_map[s[i]]

    return roman_sum

str_s = "DCCCXC"
print(roman_integer(str_s))

# T(n) : O(n)
# S(n) : O(1)