def is_palindrome(str1,start,end):
    #BASE CASE
    if start>=end:
        return True
    #WORK
    if str1[start] == str1[end]:
        # Recursive call
        return is_palindrome(str1,start+1,end-1)

    return False


s = "M12ad34am"
new_str = ""
for ch in s:
    if ch.isalpha():
        new_str += ch

print(is_palindrome(new_str.lower(),0,len(new_str)-1))






