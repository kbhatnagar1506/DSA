# bubble sort means sorting in the form of bubble

def BubbleSort(array): #[9,6,1,8,7]
    n = len(array) #5
    for i in range(n) : #loop will run 5 times # 0 #1 #2 #3 #4
        for j in range(n-i-1): #4times(when i = 0) #3times(i = 1) #2times(i=2) #1times(i=3) #0times
            if array[j]> array[j+1]:                                   #[9 , 6, 1, 8, 7]
                array[j],array[j+1] = array[j+1],array[j]              # 0   1  2  3  4
    return array 

print(BubbleSort([10,823,484,37,2737,47468,2982]))


