def check_non_decreasing(arr):
    # T(n) : O(n)
    # S(n) : O(1)

    count = 0
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            count += 1

            if count > 1:
                return False

            if i == 0 and arr[i-1] <= arr[i+1]:
                arr[i] = arr[i+1]

            else:
                arr[i+1] = arr[i]

    return True


nums = [3,4,2,5]
print(check_non_decreasing(nums))