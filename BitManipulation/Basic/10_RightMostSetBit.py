import math

def rightMostSetBit(n):
   n =  n ^ (n & (n-1))
   return int(math.log2(n)) + 1


if __name__ == "__main__":
    print(rightMostSetBit(8))
