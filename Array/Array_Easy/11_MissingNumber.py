def missing_number1(arr):
    # It only works if array doesn't contain any duplicate values
    i = 1
    # O(n)
    while i <= len(arr):
        if i != arr[i-1]:
            return i
        i += 1
    return i

def missing_number2(arr):
    n = len(arr) + 1

    # Iterate from 1 to n and check
    # if the current number is present
    for i in range(1, n + 1):
        found = False
        for j in range(n - 1):
            if arr[j] == i:
                found = True
                break

        # If the current number is not present
        if not found:
            return i
    return -1


def missing_number3(arr):
    freq = [0] * (len(arr)+2)

    for i in range(len(arr)):
        freq[arr[i]] += 1

    for i in range(1,len(arr)+2):
        if freq[i] == 0:
            return i

    return -1

def missing_num(arr):
    # XOR of a number with itself is 0 i.e.x ^ x = 0
    xor1 = 0
    xor2 = 0

    for i in range(len(arr)):
        xor1 = xor1^arr[i]

    for i in range(1,len(arr)+2):
        xor2 = xor2^i

    return xor1^xor2


nums = [1,2,3,4,5]
# nums.sort()   #O(nlogn)  for missing_number1
# print(missing_number1(nums))
print(missing_number2(nums))
print(missing_number3(nums))
print(missing_num(nums))

