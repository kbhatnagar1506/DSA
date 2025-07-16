citations = [1,3,1]
citations.sort(reverse=True)
k = 1
for i in range(0,len(citations)):
    if citations[i] <= k:
        print(citations[i])
        break
    k = k + 1
