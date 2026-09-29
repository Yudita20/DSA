def reverseBits(n):
    result = 0

    for i in range(32):
        bit = n & 1
        result = result | (bit << (31-i))
        n = n >> 1

    return result

if __name__ == "__main__":
    print(reverseBits(4))