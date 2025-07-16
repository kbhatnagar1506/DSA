import itertools
def permutations(brackets, noofcomb):
        combs = itertools.permutations(brackets , noofcomb)
        list = []
        for i in combs:
            list.append(i)
        return list 
def is_valid_parentheses(expression):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.append(char)  # Push opening bracket
        elif char in ')}]':
            if not stack or stack[-1] != matching[char]:
                return False  # Mismatch or empty stack
            stack.pop()  # Pop the matching opening bracket
    
    return len(stack) == 0  # Stack should be empty if balanced
                
def generateparenthesis(input): #input is 3 
    noofcomb = 2 * input
    bracket= ["(",")"] #bracket 
    brackets = bracket * input
    var = permutations(brackets,noofcomb)
    primarylist= []

    for i in var:
        secondarylist = []
        for j in i:
            secondarylist.append(j)
            primarylist.append(secondarylist)


    nonduplicate = []

    for i in primarylist:
        if i not in nonduplicate:
            nonduplicate.append(i)
    print(nonduplicate)
    stringlist=[]


    for i in nonduplicate:
        print(i)
        str=""
        for j in i:
            print(j)
            strlist = str+j
        stringlist.append(str)
    ans = []


    for i in stringlist:
        if is_valid_parentheses(i) == True :
            ans.append(i)            
    return ans


print(generateparenthesis(3))
        
        