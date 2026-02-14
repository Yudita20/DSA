def hashing(arr):
    hash_map = {}
    for i in range(0,len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i] , 0) + 1

    highest = float("-inf")
    lowest = float("inf")
    min_elt = None
    max_elt = None

    for key,value in hash_map.items():
        if value>highest or (highest == value and key < max_elt):
            highest = value
            max_elt = key

        if value<lowest or (lowest == value and key<min_elt):
            lowest = value
            min_elt = key

    return f"{max_elt} {min_elt}"

arr = [4,4,5,5,6]
print(hashing(arr))

