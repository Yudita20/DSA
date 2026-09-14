def combinationSumI(arr, k, index = 0,curr = None, result = None):
    if result is None:
        result = []

    if curr is None:
        curr = []

    if k < 0 or index == len(arr):
        return

    if k == 0:
        result.append(curr.copy())
        return


    # Include
    curr.append(arr[index])
    combinationSumI(arr, k - arr[index], index, curr, result)
    curr.pop()

    # Exclude
    combinationSumI(arr, k, index + 1, curr, result)

    return result

if __name__ == "__main__":
    print(combinationSumI([2,3,6,7], 7))