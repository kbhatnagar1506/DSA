def Mergesort(array):
    def merge(left,right):
        result=[]
        i=j=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                 result.append(left[i])
                 i+=1
            else:
                result.append(right[j])
                j=j+1
        result=result+left[i:]+right[j:]
        return result
    if len(array)<=1:
        return array
    mid=len(array)//2
    left=Mergesort(array[:mid])
    right=Mergesort(array[mid:])
    return merge(left,right)
   
print (Mergesort([4,62,4,6,1]))