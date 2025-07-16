s = "dsadhjpjaudfdd"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
def answer(s,words):
        map = {}
        #  making hashmap
        index = -1
        for i in s:
            index = index + 1
            if i in map:
                list = map[i]
                list.append(index)
                map[i] = list
            else:
                map[i] =[index]
        count = 0
        for word in words:
            if isvalid(word,map,s)==True :
                count = count + 1
        return count
            
def isvalid(word,map,s):
    x = 0
    array = []
    for i in word:
        if i in map and map[i] != []:
            letterindex = map[i].pop(0)
            array.append(letterindex)
            return True
        else:
            return False
s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
print(answer(s,words))