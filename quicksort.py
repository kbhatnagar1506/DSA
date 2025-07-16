def quick_sort(list3):
    less = []
    pivot= []
    more = []

    if len(list3) <= 1:
        return list3
    else:
        pivot = list3[0]
        for i in list3:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivot.append(i)

        less = quick_sort(less)
        more = quick_sort(more)
        return less + pivot + more
print(quick_sort([43,1,43,5,3,6,39,2]))