#[-1,0,1,2,-1,-4]
import itertools
def triplet(nums):
    per = []
    list = []
    n = len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if i != j and i != k and j != k:
                        if (nums[i], nums[j], nums[k])not in per:
                            if nums[i] +  nums[j] +  nums[k] == 0:
                                list.append([nums[i], nums[j], nums[k]])
                                var  =  itertools.permutations([nums[i], nums[j], nums[k]],3)
                                for w in var:
                                    per.append(w)
    return list


print(triplet([-1,0,1,2,-1,-4,-3]))

