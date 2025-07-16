s = "abcabcbb"
arr=[]
substr =""
for i in s:
    if i not in substr:
        substr = substr+ i
    elif i in substr:
        arr.append(substr)
        substr = i
final = ""
for i in arr:
    if len(i)> len(final):
        final = i
print(arr,final)

