M = (10 ** 9) + 7

def maxXor(a, b, n):
    a_xor_x = 0
    b_xor_x = 0

    for i in range(49, n-1 , -1):
        a_ith_bit = ((a >> i) & 1) > 0
        b_ith_bit = ((b >> i) & 1) > 0

        if a_ith_bit:
            a_xor_x = a_xor_x ^ (1 << i)

        if b_ith_bit:
            b_xor_x = b_xor_x ^ (1 << i)


    for i in range(n-1, -1, -1):
        a_ith_bit = ((a >> i) & 1) > 0
        b_ith_bit = ((b >> i) & 1) > 0

        if a_ith_bit == b_ith_bit:
            a_xor_x = a_xor_x ^ (1 << i)
            b_xor_x = b_xor_x ^ (1 << i)
            continue

        if a_xor_x > b_xor_x:
            b_xor_x = b_xor_x ^ (1 << i)
        else:
            a_xor_x = a_xor_x ^ (1 << i)

    a_xor_x = a_xor_x % M
    b_xor_x = b_xor_x % M

    return (a_xor_x * b_xor_x) % M


if __name__ == "__main__":
    print(maxXor(12, 5, 4))



