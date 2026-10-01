# T(n): nlog(n)
def countingBits(n):
    res = [0]*(n+1)

    for i in range(n+1):
        res[i] = i.bit_count()

    return res

def countBits(n):
    result = [0]*(n+1)

    if n == 0:
        return result

    result[0] = 0

    for i in range(1, n+1):
        if i & 1 == 1:
            result[i] = result[i // 2] + 1
        else:
            result[i] = result[i // 2]

    return result


if __name__ == "__main__":
    print(countBits(5))