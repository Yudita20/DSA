def orOperation(a, b, c):
    flips = 0

    while a != 0 or b !=0 or c != 0:
        if (c & 1) == 1:
            if (a & 1) == 0 and (b & 1 ) == 0:
                flips += 1
        else:
            if (a & 1) == 1:
                flips += 1

            if (b & 1) == 1:
                flips += 1

        a >>= 1
        b >>= 1
        c >>= 1

    return flips

if __name__ =="__main__":
    print(orOperation(2, 6, 5))


