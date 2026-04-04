import math

def find_sqrt(n):
    return int(math.sqrt(n))


def find_square(n):
    if n < 2:
        return n

    ans = 0

    low , high = 0 , n//2

    while low <= high:
        mid = (low + high)//2

        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

print(find_sqrt(28))
print(find_square(28))