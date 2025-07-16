haystack = "sadbutsad"
needle = "sad"
def indexcheck(haystack,needle):
    n = len(needle)
    for i in range(len(haystack)):
        if haystack[i:i+n]== needle:
            return i 
    return -1

print(indexcheck(haystack,needle))