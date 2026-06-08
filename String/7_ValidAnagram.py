def valid_anagrams(s , t):
    if len(s) != len(t):
        return False
    freq_map = {}
    for i in range(len(s)):
        freq_map[s[i]] = freq_map.get(s[i] , 0) + 1

    for i in range(len(t)):
        freq_map[t[i]] = freq_map.get(t[i] , 0) - 1

    for v in freq_map.values():
        if v != 0:
            return False

    return True

str_s = "anagram"
str_t = "cagaram"

print(valid_anagrams(str_s,str_t))