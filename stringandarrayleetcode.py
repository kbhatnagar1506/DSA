# def remove(nums):
#     if len(nums)<= 2:
#         return nums
    
#     k = 2

#     for i in range(2,len(nums)):
#         if nums[i] != nums[k-2]:
#             nums[k] =  nums[i]
#             k =  k + 1

#     return nums[0:k]

# print(remove([0,0,1,1,1,1,2,3,3]))
# rules of inplace :
# 1) we dont create any new storage variable 
# 2) while storage aint allowed we can create variables to keep track
# 3) you will iterate on the current storing object and make it output-like 
# 4) all operations on the preexisiting variables


# code prompt: you'll understand the implementation 
# out put and conditional 
# what could be the easiest implementation
# implementation in accordance with big o notation and storage complexity 
# you'll write the code 


# first two elements that will be agar 2 - 2 diff toh bhi array 2 same toh bhi array conditional output array of two 
# second implementation according to the prompt we'll code it 