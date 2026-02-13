# Iterative method
n = int(input("Enter a number:"))
for i in range(n):
    print("Hi",end=" ")


# Recursive method
def printName(num):
    # BASE CASE
    if num == 0:
        return

    # WORK
    print("Hello",end=" ")

    # FUNCTION CALL(RECURSIVE FUNCTION)
    printName(num-1)

n = int(input("Enter a number:"))
printName(n)