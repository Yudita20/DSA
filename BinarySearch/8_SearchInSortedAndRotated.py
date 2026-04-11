def binary_search(arr , tar , s , e):
    while s <= e:
        mid = (s+e) // 2
        if arr[mid] == tar:
            return mid
        elif arr[mid] > tar:
            e = mid - 1
        else:
            s = mid + 1
    return -1

def rotated_and_sorted(arr , tar):
    s = 0
    e = len(arr)-1

    i = 0
    while i < len(arr)-1:
        if arr[i] > arr[i+1]:
            left = binary_search(arr , tar , s , i)
            right = binary_search(arr, tar , i+1 , e)

            if left < 0:
                return right
            elif right < 0:
                return left
        i += 1

    return binary_search(arr,tar,s,e)


def search(arr,k):
    s , e = 0 , len(arr)-1

    while s <= e:
        mid = (s+e)//2

        if arr[mid] == k:
            return mid

        if arr[s] <= arr[mid]:
            if arr[s] <= k < arr[mid]:
                e = mid - 1
            else:
                s = mid + 1

        else:
            if arr[mid] < k <= arr[e]:
                s = mid + 1
            else:
                e = mid -1

    return -1


nums = [4,5,6,7,8,0,1,2,3]
print(rotated_and_sorted(nums,1))
print(search(nums,5))



