class Python:
    def __init__(self):
        print(end="")

    def reverse_an_array(self,arr,start,end):
        # BASE CASE
        if start >= end:
            return arr

        #WORK
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp

        #Recursive call
        return self.reverse_an_array(arr,start+1,end-1)

sol = Python()
arr = [8,9,5,6,1]
print(sol.reverse_an_array(arr,0,len(arr)-1))



# Built_in function
arr = [8,9,5,6,1]
arr[:] = arr[::-1]
print(arr)