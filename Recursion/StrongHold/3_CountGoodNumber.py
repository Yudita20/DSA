MOD = 10**9 + 7

def findPower(a , b):
    if b == 0:
        return 1

    half = findPower(a , b//2)
    result = (half * half) % MOD

    if b % 2 != 0:
        result = (result * a) % MOD

    return result

def countGoodNumber(n):
    return findPower(5, (n+1)/2) * findPower(4, n/2)

if __name__ == "__main__":
    print(countGoodNumber(5))
