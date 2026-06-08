def rotate_string(s,goal):
    if len(s) != len(goal):
        return False

    doubled_s = s + s
    return goal in doubled_s

str_s = "abcde"
str_goal = "adeab"
print(rotate_string(str_s,str_goal))