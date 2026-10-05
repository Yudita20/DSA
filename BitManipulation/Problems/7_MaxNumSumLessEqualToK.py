# LeetCode 3007
import math

def countXposBits(num, x):
    cnt = 0
    while num != 0:
        if (num >> (x-1)) & 1 != 0:
            cnt += 1
        num = num >> x

    return cnt

def max_number_k(k, x):
    acc_price = 0

    num = 1
    while True:
        price = countXposBits(num, x)
        if acc_price + price > k:
            break
        else:
            acc_price += price
        num += 1

    return num-1


def getBitsCount(num):
    bit_length = int(math.log2(num))
    nearest_power_two = (1 << bit_length) # pow(2, bit_length)
    bit_count = []

    bit_count[bit_length] += num - nearest_power_two + 1

    for i in range(0, bit_length + 1):
        bit_count[i] += nearest_power_two // 2

    num -= nearest_power_two
    getBitsCount(num)


def findMaximumNumber(k, x):
    left = 0
    right = 1e15

    result = 0

    while left <= right:
        mid = left + (right - left) // 2
        # Count set bits at each position from 0 to mid
        getBitsCount(mid)

if __name__ == "__main__":
    print(max_number_k(9, 1))








