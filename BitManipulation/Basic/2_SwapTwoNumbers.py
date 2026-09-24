def swapNumbers(a, b):
    a = a ^ b
    b = a ^ b
    a = b ^ a

    return a, b

if __name__ == "__main__":
    n1, n2 = swapNumbers(25, 28)
    print(f"a : {n1}, b : {n2}")