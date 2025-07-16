# def majyority(nums):
#     major = len(nums)//2
#     dict = {}
#     for i in nums:
#         if i in dict:
#             dict[i] = dict[i] + 1 
#         else:
#             dict[i] = 1
#     for i in dict:
#         if dict[i] > major:
#             return (i)
# print(majyority([2,2,1,1,1,2,2]))

# nums = [1,2,3,4,5,6,7,8]
# k = 3
# k = k
# print(nums[-k:]+nums[:-k])


# list = [7,6,4,3,1]
# k = 0 
# for i in range(1,len(list)):
#     list[k] = list [i] -  list[k]
#     k = k + 1

# profit = 0 
# for i in range(0,len(list)-1):
#     if list[i] > 0:
#         profit = profit + list[i]

# print(profit)



# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
# arr = [2,3,1,1,4]
# currentindex = arr[0]
# for i in arr[arr[0]:]


# 🧪 Example 1: citations = [3, 0, 6, 1, 5]
# Sort the array:
# [0, 1, 3, 5, 6]

# Now go from highest to lowest to find how many papers have ≥ h citations.

# h	How many papers have ≥ h citations?
# 5	1 paper → ❌
# 4	2 papers → ❌
# 3	3 papers → ✅ (papers with 3, 5, 6)
# 2	4 papers → ✅
# 1	5 papers → ✅

# But we want the maximum h that satisfies the condition:
# So the answer is 3

