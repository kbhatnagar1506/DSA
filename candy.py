def candy(ratings):
    answer = [1]*len(ratings)
    for i in range(1,len(ratings)):
        if ratings[i]>ratings[i-1]:
                answer[i] = answer[i-1] + 1
    for i in range(len(ratings)-2,-1,-1):
        if ratings[i] > ratings[i+1]:
            answer[i] = max(answer[i], answer[i + 1] + 1)
    return (answer)
        

        
print(candy([1,9,8,6,1]))

