def removeBit(n):
    return n & (n-1)

if __name__ == "__main__":
    print(removeBit(15))