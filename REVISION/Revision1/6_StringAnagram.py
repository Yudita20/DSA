def is_anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        freq_map  = {}
        for ch in s1.lower():
            freq_map[ch] = freq_map.get(ch,0)+1

        for ch in s2.lower():
            if ch not in freq_map:
                return False
            freq_map[ch] -= 1

        for val in freq_map.values():
            if val != 0:
                return False
        return True

print(is_anagram("aabb","ccdd"))

