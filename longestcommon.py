strs = ["flower","flow","flight"]
string = strs[-1]
index = 0 
dict = {}
for i in range(len(strs)):
    if len(strs[i]) < len(string):
        string = strs[i]
        index = i
strs[index] = strs[-1]
strs.pop()
str =""
for i in strs:
    for j in range(len(string)):
        if string[:j] == i[:j]:
            str = i[:j]
print(str)
