def setBit(n, i):
    return n | (1 << i)

if __name__ == "__main__":
    print(setBit(13, 2))
    print(setBit(9, 1))