class Python:
    def __init__(self):
        print(end="")

    def print_numbers(self,n):
        if n == 0:
            return
        self.print_numbers(n-1)
        print(n,end=" ")

sol = Python()
sol.print_numbers(5)

