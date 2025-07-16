def main(words,maxwidth):
    dict ={}
    list = []
    index = 0
    count = 0
    for i in words:
        if count < maxwidth:
            count = count + len(i) + 1
            list.append(i)
        if count > maxwidth:
            j = list.pop()
            dict[count-len(j)-1-len(list)] = list
            list = [i]
            count = len(i)
            index = index + 1
    count = 0
    for i in list:
        count = count + len(i)
    dict[count] = list

    #####################################
    #NOW CONVERTING INTO LIST WITH STRINGS
    solution = []
    for i in dict:
        spacingleft = maxwidth - i
        noofwords = len(dict[i])
        str = ""
        if noofwords != 1:
            distribute = spacingleft//(noofwords-1)
        else:
            distribute = spacingleft//noofwords
        space = ' ' * distribute
        list1 = dict[i]
        for j in dict[i]:
            if dict[i] != list:
                if list1[-1] != j:
                    str = str+j+space
                else:
                    str = str + j
            else:
                if list1[-1] == j:
                    str = str+j+space
                else:
                    str = str + j + " "
                
        solution.append(str)
    print(solution)

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

main(words,maxWidth)

