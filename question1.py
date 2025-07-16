# [30,38,30,36,35,40,28] [1,4,1,2,1,0,0]
# 3 options
# find the next greater no 
# allot count 
# or aLLOT 0 
# container where we will store where i will store the first value and ill compare that container to every element until i find anything bigger than that 
#ill count the no of times i've compared it 
#and return the count 


list= [73, 74, 75, 71, 69, 72, 76, 77]

stack = []
n = len(list)
for i in range(0,n):
    count = 1
    for j in range(i+1,n):
        if list[i] < list[j]:
            stack.append(count)
            break
        elif list[i] > list[j]:
            count= count + 1
            if j == n-1:
                stack.append(0)
stack.append(0)

print(stack)
        # agar kuch nhi h agge badda toh zero to the shit

            

            





