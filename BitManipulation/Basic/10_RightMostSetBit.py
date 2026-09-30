def rightMostSetBit(n):
   return n ^ (n & (n-1))

if __name__ == "__main__":
    print(rightMostSetBit(12))
