def minimumFlips(start, goal):
    n = start ^ goal

    cnt = 0
    while n != 0:
        cnt += n & 1
        n = n >> 1

    return cnt


if __name__ == "__main__":
    print(minimumFlips(10, 7))