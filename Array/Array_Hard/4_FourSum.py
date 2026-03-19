def four_sum(arr,target):
    arr.sort()
    res = []

    for x in range(len(arr)):
        if x>0 and arr[x] == arr[x-1]:
            continue

        for y in range(x+1,len(arr)):
            if y>x+1 and arr[y] == arr[y-1]:
                continue

            left = y+1
            right = len(arr)-1

            while left<right:
                total = arr[x]+arr[y]+arr[left]+arr[right]

                if total == target:
                    res.append([arr[x],arr[y],arr[left],arr[right]])
                    left += 1
                    right -=1

                    while left<right and arr[left] == arr[left-1]:
                        left += 1
                    while left<right and arr[right] == arr[right+1]:
                        right -= 1

                elif total>target:
                    right -= 1
                else:
                    left += 1

    return res


# nums = [1,0,-1,0,-2,2]
nums = [2,2,2,2,2]
print(four_sum(nums,8))


