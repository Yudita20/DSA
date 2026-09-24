def setOrNot(n, i):
    # Left shift
    if (n & (1 << i)) == 0:
        return False
    return True

    # Right Shift
    # if ((n >>i) & 1) == 1:
    #     return True
    # return False


if __name__ == "__main__":
    print(setOrNot(13, 1))
