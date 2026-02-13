def fib(n,f,s,c):
    #Base case
    if c == n:
        return

    #work
    print(f,end=" ")

    #Recursive call
    fib(n,s,f+s,c+1)

fib(5,0,1,0)

