def subsetsII(arr, index = 0, curr = None, result = None):
    if result is None:
        result = []

    if curr is None:
        curr = []

    result.append(curr.copy())

    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue

        curr.append(arr[i])
        subsetsII(arr, i + 1, curr, result)
        curr.pop()

    return result

if __name__ == "__main__":
    nums  = [1,1,2]
    nums.sort()
    print(subsetsII(nums))
