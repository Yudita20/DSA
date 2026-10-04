def minFlips(n):
    r = 31
    f_value = [0] * r
    f_value[0] = 1

    for i in range(1, 31):
        f_value[i] = (2 * f_value[i-1]) + 1

    result = 0
    sign = 1

    for i in range(30, -1, -1):
        ith_bit = (1 << i) & n

        if ith_bit == 0:
            continue

        if sign > 0:
            result += f_value[i]
        else:
            result -= f_value[i]

        sign *= -1

    return result


if __name__ == "__main__":
    print(minFlips(3))


