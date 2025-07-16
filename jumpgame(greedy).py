def jumpgame(nums):#[3,1,1,0,4]
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest , i + nums[i])
    return True
