s = "A man, a plan, a canal: Panama"
def palindrome(s):
    s = s.lower()
    string ="abcdefghijklmnopqrstuvwxyz"
    final = ""
    for i in s:
        if i in string:
            final = final + i 
    x = 0 
    for i in range(0,(len(final)//2)):
        if final[i] == final[len(final) -1 -i]: 
            x =x +1

    if x == len(final)//2:
        return (True)
    else:
        return False

