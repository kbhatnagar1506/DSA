def mergeSort(array):
    def merge(left, right):  #merge takes input of half of the first half and second half
        result = []             # result array
        i = j = 0
        while i < len(left) and j < len(right): #loop logic until the array left and right exhausts
            if left[i] <= right[j]:             # comparison when right is bigger
                result.append(left[i])          #incrementing left loop
                i += 1                          # incrementing the left loop
            else:                               #comparison when left is bigger
                result.append(right[j])         #appending right one by one
                j += 1                          # incrementing the right loop
        result = result + left[i:] + right[j:] # combining rest of the array
        return result                            # returning result array to merge sort array
    if len(array) <= 1:
        return array                                #returning the final array
    mid = len(array) // 2 # diving the array into half
    left = mergeSort(array[:mid])           #giving first half
    right = mergeSort(array[mid:])          #giving the secong half
    return merge(left, right)               #combine sorting the the first and second half
print(mergeSort([6,3,26,8,3]))              