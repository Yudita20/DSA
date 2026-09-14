def combinationSumII(arr, target, index = 0, curr = None, result = None):
    if result is None:
        result = []

    if curr is None:
        curr = []

    if target == 0:
        result.append(curr.copy())
        return

    for i in range(index, len(arr)):
        if i > index and arr[i] == arr[i-1]:
            continue


        if arr[i] > target:
            break

        curr.append(arr[i])
        combinationSumII(arr, target - arr[i], i + 1, curr, result)
        curr.pop()

    return result

if __name__ == "__main__":
    print(combinationSumII(sorted([2, 1, 2, 7, 6, 1, 5]), 8))