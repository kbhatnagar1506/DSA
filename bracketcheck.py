def check(str):
    stack = []
    dict=  {"{":"}","[":"]","(":")"}
    count  = 0 
    for i in str:
        stack.append(i)
    n = len(stack)
    while stack != []:
        value =  stack.pop()
        for i in dict:
            if dict[i] == value and i in stack: 
                stack.remove(i)
                count = count + 2
    if count == n:
        print("valid")
    else:
        print("invalid")
                
check("()()")