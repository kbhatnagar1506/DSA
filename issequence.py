# Input: s = "abc", t = "ahbgdc"
# Output: true
s = "abc"
t = "ahbgdc"
def issequence(s,t):
    sCursor = 0 
    for i in t :
        if s[sCursor] == i:
            sCursor = sCursor + 1
    if sCursor == len(s):
        return (True)
    else:
        return False
