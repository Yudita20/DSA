def search_in_rotated_and_sortedII(arr,tar):
    left , right = 0 , len(arr)-1

    while left <= right:
        mid = (left+right)//2

        if arr[mid] ==tar:
            return True

        while arr[mid] == arr[left] == arr[right]:
            left += 1
            right -= 1

        if arr[left] <= arr[mid]:
            if arr[left] <= tar <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if arr[mid] <= tar <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1


    return False


nums = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
print(search_in_rotated_and_sortedII(nums,7))

