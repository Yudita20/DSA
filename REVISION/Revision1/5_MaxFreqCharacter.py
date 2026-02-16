def character_hashing(s):
    freq_map = {}
    for ch in s:
        freq_map[ch] = freq_map.get(ch , 0) + 1

    max_freq = float("-inf")
    wo =""
    for ch in s:
        if freq_map[ch] > max_freq:
            max_freq = freq_map[ch]
            wo = ch
    return wo

s1 = "aaaaaabbbc"
print(character_hashing(s1))