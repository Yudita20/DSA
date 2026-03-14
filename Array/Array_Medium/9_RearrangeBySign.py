def brute(arr):
    n = len(arr)//2
    neg = []*n
    pos = []*n
    for i in range(len(arr)):
        if arr[i] > 0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])

    for i in range(n):
        arr[2*i] = pos[i]
        arr[2*i + 1] = neg[i]

    return arr


def better(arr):
    res = [0]*len(arr)
    pos_idx = 0
    neg_idx = 1
    for i in range(len(arr)):
        if arr[i] > 0:
            res[pos_idx] = arr[i]
            pos_idx += 2
        else:
            res[neg_idx] = arr[i]
            neg_idx += 2

    return res

nums = [1,2,-4,-5]
print(brute(nums))
print(better(nums))