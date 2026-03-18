def majority_element(arr):
    res = []
    hash_map = {}
    for i in range(len(arr)):
        hash_map[arr[i]] = hash_map.get(arr[i],0) + 1

    for key,value in hash_map.items():
        if value > len(arr)//3:
            res.append(key)
    return res


def majority_elementII(arr):
    count1 , count2 = 0 , 0
    elt1 , elt2 = -1 , -1
    res = []

    for i in range(len(arr)):
        if arr[i] == elt1:
            count1 += 1

        elif arr[i] == elt2:
                count2 += 1

        elif count1 == 0:
            elt1 = arr[i]
            count1 += 1

        elif count2 == 0:
            elt2 = arr[i]
            count2 += 1

        else:
            count1 -= 1
            count2 -= 1

    c1 = arr.count(elt1)
    c2 = arr.count(elt2)

    if c1 > len(arr)//3:
        res.append(elt1)
    if c2 > len(arr)//3 and elt2 != elt1:
        res.append(elt2)

    return res

nums = [-1,-1,-1]
print(majority_elementII(nums))