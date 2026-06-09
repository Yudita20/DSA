def sort_characters(s):
    hash_map = {}

    for ch in s:
        hash_map[ch] = hash_map.get(ch , 0) + 1

    arr = []
    for key , value in hash_map.items():
        arr.append((value , key))

    arr.sort(key=lambda x:-x[0])

    res = []
    for freq,ch in arr:
        res.append(freq*ch)

    return "".join(res)

str_s = "mississippi"
print(sort_characters(str_s))

