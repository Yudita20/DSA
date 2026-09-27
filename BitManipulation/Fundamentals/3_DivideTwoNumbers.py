INT_MAX = (2 ** 31) - 1
INT_MIN = -2 ** 31


def divideTwoNumbers(dividend, divisor):
    negative = (dividend < 0) != (divisor < 0)

    divisor_abs = abs(divisor)
    dividend_abs = abs(dividend)

    quotient = 0

    while dividend_abs >= divisor_abs:
        cnt = 0

        while dividend_abs >= (divisor_abs << (cnt + 1)):
            cnt += 1

        quotient += 1 << cnt
        dividend_abs = dividend_abs - (divisor_abs << cnt)

    result = -quotient if negative else quotient

    if result > INT_MAX:
        return INT_MAX

    if result < INT_MIN:
        return INT_MIN

    return result

if __name__ == "__main__":
    print(divideTwoNumbers(10, 3))