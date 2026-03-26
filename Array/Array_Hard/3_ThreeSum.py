def three_sum(arr):
    arr.sort()
    res = []

    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr)-1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == 0:
                res.append([arr[i],arr[left],arr[right]])
                left += 1
                right -= 1

                while left<right and arr[left] == arr[left-1]:
                    left += 1

                while left<right and arr[right] == arr[right+1]:
                    right -= 1

            elif total<0:
                left += 1
            else:
                right -= 1

    return res


nums = [-1,0,1,2,-1,-4,0,2]
print(three_sum(nums))