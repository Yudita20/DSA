def floor(arr,tar):
    s , e = 0 , len(arr)-1
    ans = -1

    while s <= e:
        mid = (s+e)//2

        if arr[mid] <= tar:
            ans = arr[mid]
            s = mid+1
        else:
            e = mid-1

    return ans

def ceil(arr,tar):
    s, e = 0, len(arr) - 1
    ans = -1

    while s <= e:
        mid = (s + e) // 2

        if arr[mid] >= tar:
            ans = arr[mid]
            e = mid-1
        else:
            s=mid+1

    return ans

def main(arr,tar):
    f = floor(arr,tar)
    c = ceil(arr,tar)

    return f"{f},{c}"

nums = [3, 4, 4, 7, 8, 10]
print(main(nums,5))