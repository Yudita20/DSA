def countSubK(arr, k, index=0, curr_sum=0):
    if index == len(arr):
        if curr_sum == k:
            return 1
        else:
            return 0

    return (countSubK(arr, k, index + 1, curr_sum + arr[index]) +
            countSubK(arr, k, index + 1, curr_sum))


def subsequencesWithSumK(arr, k, index = 0, curr_sum = 0, curr = None, result = None):
    if result is None:
        result = []

    if curr is None:
        curr = []

    if index == len(arr):
        if curr_sum == k:
            result.append(curr.copy())
        return


    # Include
    curr.append(arr[index])
    subsequencesWithSumK(arr, k, index + 1, curr_sum + arr[index], curr, result)
    curr.pop()

    # Exclude
    subsequencesWithSumK(arr, k, index + 1, curr_sum, curr, result)

    return result

def anySubsequenceWithSumK(arr, k, index = 0, curr_sum = 0):
    if index == len(arr):
        # Condition Satisfied
        if curr_sum == k:
            return True
        # Condition not satisfied
        else:
            return False

    if anySubsequenceWithSumK(arr, k, index + 1, curr_sum + arr[index]):
        return True

    if anySubsequenceWithSumK(arr, k, index + 1, curr_sum):
        return True

    return False

if __name__ == "__main__":
    # print(countSubK([1,1,1], 3))
    # print(subsequencesWithSumK([1, 1, 2], 2))
    print(anySubsequenceWithSumK([4,3,9,2],10))
