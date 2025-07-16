# def bubblesort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j+1]<array[j]:
#                 array[j], array[j+1] = array[j+1],array[j]
#     return array

# def selectionsort(array):
#     n = len(array)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1,n):
#             if array[min_index] > array[j]:
#                 min_index = j
#         if min_index != i:
#             array[i],array[min_index] = array[min_index] , array[i]

#     return array

# def insertsort(array):
#     n = len(array)
#     for step in range(1,n):
#         key = array[step]
#         j = step-1
#         while j >= 0 and key < array[j]:
#             array[j+1]=array[j]
#             j = j -1
#         array[j+1] = key
#     return array
# print(insertsort([6,3,26,8,3]))
    

def quicksort(arr):
    less=[]
    pivot=[]
    more=[]
    if len(arr) <= 1:
        return arr
    else:
        pivotno = arr[0]
        for i in arr:
            if pivotno > i:
                less.append(i)
            elif pivotno < i:
                more.append(i)
            else:
                pivot.append(i)
    less = quicksort(less)
    more = quicksort(more)
    return less + pivot + more
print(quicksort([6,3,26,8,3]))
        

