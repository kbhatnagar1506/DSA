def selectionsort(arr): #[3,2,1,6,4]
    # what is selection sort - ss is sorting algorithm which sorts an array by sorting one by one numbers on minimum index where minimum index once goes through every possible index in an array
    # we will define that how many times should our algorithm run for 
    n = len(arr) # 5
    for i in range(n-1): # 0 1 2 3 
    # define minimun index - which will go through every index possible in the array one by one
        min_index = i 
        #here the algorithm in j will run from 1+ index (current index) of the minimum index as we gotta compare
        for j in range(i+1,n):
            if arr[j]<arr[min_index]: #if our minimum index which is supposed to be smallest is lets say bigger than j(cursor(current index))
                min_index = j
    # we will check wether the current index is minimum index or not 
        if min_index != i :
    # if not then we will sort and we will replace the current  with the minimum index 
            arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
#call statement
print(selectionsort([3,2,1,6,4]))
