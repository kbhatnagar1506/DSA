# def ContainDuplicate(list):
#     x = 0 
#     n = len(list)
#     for i in range(0,n):
#         for j in range(i+1,n):
#             if list[i] == list[j]:
#                 return True
#     return False
                
            
# print(ContainDuplicate([1,84,32,66,84]))

# def anagram(s,t):
#     lst = []
#     for i in s:
#             lst.append(i)
#     for i in t:
#         if i in lst:
#             lst.remove(i)
#     if lst == []:
#         return True 
#     else:
#         return False
# print(anagram("anagram","nagaram"))


# def sum(array,target):
#     for i in range(0,len(array)):
#         for j in range(i+1,len(array)):
#             if array[i] + array[j]  == target:
#                 return (f"[{i},{j}]")
# print(sum([2,7,11,15],9))

# def groupanagram(ListOfWords):
#     finallist = []
#     n = len(ListOfWords)
#     for i in range(0,n):
#         currentlist =[ListOfWords[i]]
#         for j in range(i+1,n):
#             if anagram(ListOfWords[i],ListOfWords[j])==True:
#                 currentlist.append(ListOfWords[j])
#         finallist.append(currentlist)
#     return finallist    
# print(groupanagram(["eat","tea","tan","ate","nat","bat"]))

# def top(nums , k):
#     dict = {}
#     n = len(nums)
#     for i in range(0,n):
#         counter = 0
#         for j in range(0,n):
#             if nums[i]==nums[j]:
#                 counter = counter + 1
#         dict[nums[i]] = counter


#     list = []
#     for i in dict.values():
#         list.append(i)
#     length = len(list)
#     for i in range(length):
#         for j in range(length-i-1):
#             if list[j] < list[j+1]:
#                 list[j],list[j+1]= list[j+1],list[j]
#     anslist = []  
#     while k > 0 :
#         var = list.pop(0)
#         for i in dict:
#             if dict[i] == var:
#                 anslist.append(i)
#         k = k -1
#     print(anslist)
# nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3,9,8,0,1,2,4,4,4,4,4,10,10,10,10,10,10,10,5,5,5,5,5,5,5,5,5,1001010101,102002030]
# k = 3
# top(nums,k)

# def array(arr):
#     dict = {}
#     ans = []
#     n = len(arr)
#     for i in arr:
#         dict[i] = 1
#     x = 0
#     while x < n:
#         number = arr.pop(x)
#         for i in arr:
#             if i != number :
#                 dict[number] = dict[number] * i
#         arr.insert(x,number)
#         x = x + 1
#     for i in dict:
#         ans.append(dict[i])
#     print(ans)
# array([1,2,3,4])


# def parantheses(str):# defined the function
#     dict = {"{":"}","[":"]","(":")"} # defined the dict 
#     stack =[ ] # stack implementation
#     x = 0 #x =0
#     for i in str: #{}[]())
#         stack.append(i)
#     while stack != []: 
#         bracket = stack.pop(-1) #poped --> )
#         for i in dict: # ( [ { 
#             if bracket == dict[i]: # ) ( = )
#                 if i in stack: 
#                     stack.remove(i)
#                     x = x + 2 #x = 8
#     if x == len(str):
#         return True
#     else:
#         return False
# print(parantheses("()[[}{]]"))


# def sudokucheck(board):
#     num = ["1","2","3","4","5","6","7","8","9"]
#     for i in board:
#         for k in range(0,len(i)):
#                 for l in range(k+1,len(i)):
#                     if i[k] in num and i[l]in num: 
#                         if i[k] == i[l]:
#                             print("common element in row")
#     NoOfColumn= 8
#     y= 0 
#     while y < NoOfColumn:
#         x = 0 
#         while x < NoOfColumn : 
#             if (board[x][y]) == (board[x+1][y]):
#                 print(board)
#             x = x + 1
#     y = y + 1

# sudokucheck(board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# )


def LongestConsecutiveInteger(arr):
    dict ={}
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            if arr[j] == arr[i]+1:
                dict[i] = [arr[i],arr[j]]
    return dict
print(LongestConsecutiveInteger([2,20,4,10,3,4,5]))

        
