def check_palindrome(st,start,end):
    #BASE CASE
    if start>=end:
        return True

    #WORK
    if st[start] == st[end]:
        # RECURSIVE CALL
        return check_palindrome(st,start+1,end-1)
    else:
        return False


str1 = input("Enter a string : ")
new_str = ""
for ch in str1:
    if ch.isalpha():
        new_str += ch

print(check_palindrome(new_str.lower(),0,len(new_str)-1))





