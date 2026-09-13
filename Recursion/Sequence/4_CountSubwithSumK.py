def countSubK(arr, k, index=0, curr_sum=0):
    if index == len(arr):
        if curr_sum == k:
            return 1
        else:
            return 0

    return (countSubK(arr, k, index + 1, curr_sum + arr[index]) +
            countSubK(arr, k, index + 1, curr_sum))


if __name__ == "__main__":
    print(countSubK([1,1,2], 2))
