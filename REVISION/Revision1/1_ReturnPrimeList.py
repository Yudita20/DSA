import math

def is_prime(n):
    if n == 1:
        return
    for i in range(2, (int(math.sqrt(n)) + 1)):
        if n % i == 0:
            return 0

    return 1


def prime_list(arr):
    res = []
    for i in range(0, len(arr)):
        if is_prime(arr[i]) == 1:
            res.append(arr[i])

    return res

arr = [2,3,4,5,6,7,8,9]
print(prime_list(arr))





