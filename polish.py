def operate(a,b,op):
    operation  = {"+": a + b,"-":a-b,"/":a/b,"*":a*b}
    for i in operation:
        if i  == op:
            return operation[i]
list=["+","-","8"]
str = "5 1 2 + 4 × + 3 −"
a = str.split( )
stack = []
i=0


