class Python:
    def __init__(self,str):
        self.number_hashing(arr)
        self.character_hash(str)

    def number_hashing(self,arr1):
        hash_arr = [0]*13
        for i in range(0 , len(arr1)):
            hash_arr[arr1[i]] += 1

        print(hash_arr)

    #for lowercase characters
    def character_hash(self,str1):
        hash_arr = [0] * 26
        for ch in str1:
            asc = ord(ch)
            index = asc - 97
            hash_arr[index] += 1

        print(hash_arr)



arr = [1,2,1,3,2]
st = "abcdabefc"
sol = Python(st)



