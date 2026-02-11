#Concept used:
# last_digit = num % 10
# remove_digit = num // 10

num = int(input("Num = "))
count = 0

num = abs(num)    #Handle negative numbers

if num == 0:     #0 as edge case
    print(1)

while num>0:
    count += 1
    num = num // 10

print(count)


