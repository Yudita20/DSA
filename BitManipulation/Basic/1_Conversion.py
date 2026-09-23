def decimalToBinary(num):
    b = ""
    while num >= 1:
        if num % 2 == 0:
            b += "0"
        else:
            b += "1"

        num = num // 2

    return b[::-1]

def binaryToDecimal(num_str):
    d = 0
    p = 1
    for i in range(len(num_str)-1, -1, -1):
        if int(num_str[i]) == 1:
            d = d + int(num_str[i]) * p
        p *= 2
    return d

if __name__ == "__main__":
    print(decimalToBinary(8))
    print(binaryToDecimal("1001"))