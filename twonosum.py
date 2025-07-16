def sum(input, target):
    lst = []
    for i in input:
        if i < target:
            lst.append(i)
    n = len(lst)
    ans = []
    for i in range(0,n):
        for j in range(i,n):
            if lst[i]+ lst[j] == target and lst[i] != lst[j]:
                if [lst[i],lst[j]] not in ans and [lst[j],lst[i]] not in ans :
                    ans.append([lst[i],lst[j]])
    return ans

print(sum([1,2,3,4,5,5,5,5,11,5,5,7,9,9,8,7,6,5,4,4,32,56,7,3,2,9,2,2,3,6,9],10))