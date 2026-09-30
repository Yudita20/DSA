def orOperation(a, b, c):
    flip = 0

    while a != 0 or b !=0 or c != 0:
        if (c & 1) == 1:
            if (a & 1) == 0 and (b & 1 ) == 0:
                flip += 1
        else:
            if (a & 1) == 1:
                flip += 1

            if (b & 1) == 1:
                flip += 1

        a >>= 1
        b >>= 1
        c >>= 1

    return flip

if __name__ =="__main__":
    print(orOperation(2, 6, 5))


