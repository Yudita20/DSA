def powerOfTwo(n):
    if n <= 0:
        return False

    if n & (n-1) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    for num in range(10):
        print(powerOfTwo(num))