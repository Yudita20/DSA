def countSetBits(n):
    cnt = 0
    while n != 0:
        n = n & (n-1)
        cnt += 1
    return cnt

def countSetBit(n):
    cnt = 0
    while n != 0:
        cnt += n & 1
        n = n >> 1

    return cnt

if __name__ == "__main__":
    print(countSetBit(13))
    print(countSetBits(13))


