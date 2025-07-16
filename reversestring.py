from arraymodule import Array
def reverse_string(string):
        arr = Array([]) 
        rev_string = "" 
        for i in string:
            arr.shift(0,i)
        rev_array = arr.view()
        for i in rev_array :
            rev_string= rev_string + i
        return (rev_string)
print(reverse_string("uddak sekil udaa"))