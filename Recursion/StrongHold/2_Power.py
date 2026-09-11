def powerFunction(x , n):
    if n == 0:
        return 1

    if n < 0:
        return 1/powerFunction(x , abs(n))

    half = powerFunction(x , n//2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x



if __name__ == "__main__":
    print(powerFunction(2, 10))
