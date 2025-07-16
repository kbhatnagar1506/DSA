nums = [-1,0,1,2,-1,-4]
def sum3(nums):
    nums.sort()
    res = []
    for i in nums:
        target = -i
        left = 0
        right = len(nums)-1
        while right > left:
            sum = nums[right]+nums[left]
            if sum == target:
                res.append([i,nums[left],nums[right]])
                left = left +1 
                right = right - 1
            elif sum > target:
                right = right - 1 
            else :
                left = left + 1 

    return res
print(sum3(nums))