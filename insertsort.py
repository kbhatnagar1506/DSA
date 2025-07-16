def insertionsort(array):
    for step in range(1,len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and array[j]>key:
            array[j+1]=array[j]
            j = j -1
        array[j+1]=key
    return array
print(insertionsort([10,1,9,4,7,4]))