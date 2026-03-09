def number_appears_one(arr):
    xor = 0
    for i in range(len(arr)):
        xor = xor ^ arr[i]

    return xor

def number_once_appear(arr):
    freq ={}
    for i in range(len(arr)):
        freq[arr[i]] = freq.get(arr[i],0) + 1

    for key,value in freq.items():
        if value == 1:
            return key

    return -1


nums = [4,1,2,1,2]
print(number_appears_one(nums))
print(number_once_appear(nums))