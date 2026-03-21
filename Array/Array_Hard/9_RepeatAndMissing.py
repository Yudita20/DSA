def repeat_and_missing(arr):
    missing , repeating = -1 , -1
    hash_map = {}
    for i in range(len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i],0)+1

    for key,value in hash_map.items():
        if value > 1:
            repeating = key

    for i in range(1,len(arr)+1):
        if i not in hash_map:
            missing = i

    return [repeating , missing]


nums = [1,1,2,3,4,5]
print(repeat_and_missing(nums))
