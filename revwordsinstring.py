s = "  hello world  "
list = s.split()
str =""
for i in range(len(list)-1,-1,-1):
    if i != 0:
        str = str + list[i] + " "
    else:
        str = str + list[i]
print(str)