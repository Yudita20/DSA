n = int(input("num = "))
flag = 1

if n == 1:
    print("Neither prime nor composite")

else:
    for i in range(2 , int(n**0.5 + 1)):
        if n%i == 0:
            flag = 0
            break

    if flag:
        print("Prime")
    else:
        print("Not prime")
