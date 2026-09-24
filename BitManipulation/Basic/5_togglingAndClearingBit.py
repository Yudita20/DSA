def clearBit(n, i):
    return n & ~(1 << i)

def togglingBit(n, i):
    return n ^ (1 << i)

if __name__ == "__main__":
    print(clearBit(13, 2))
    print(togglingBit(9, 2))