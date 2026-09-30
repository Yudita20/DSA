import math

def rightMostSetBit(n):
   right_most_bit =  n ^ (n & (n-1))
   return right_most_bit, int(math.log2(right_most_bit)) + 1


if __name__ == "__main__":
    print(rightMostSetBit(12))
