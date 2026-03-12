# Problem : Majority Element (LC:169)
# Approach : Boyer–Moore Majority Vote Algorithm

def majority_element(arr):
    n = len(arr)//2
    for i in range(len(arr)):
        count = 1
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > n:
            return arr[i]
    return -1

def majority_better(arr):
    n = len(arr)//2
    hash_map = {}
    for i in range(len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i],0) + 1

    for key,value in hash_map.items():
        if value > n:
            return key

    return -1


def majority_optimal(arr):
    count = 0
    elt = None
    for i in range(len(arr)):
        if count == 0:
            count = 1
            elt = arr[i]

        elif arr[i] == elt:
            count += 1
        else:
            count -= 1

    c = arr.count(elt)
    if c > len(arr)//2:
        return elt
    return -1


nums = [7,0,0,1,2,2,2,7,7]
print(majority_element(nums))
print(majority_better(nums))
print(majority_optimal(nums))
