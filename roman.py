roman_dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
s= "MCMXCIV"
x = 0
roman_list = []
for i in s:
    roman_list=roman_list+[i]
for i in range(0,len(roman_list)):
    if roman_list[i] == "V" and roman_list[i-1] == "I":
        x = x - 1
        x = x + 4
    elif roman_list[i] == "X" and roman_list[i-1] == "I":
        x = x - 1
        x = x + 9
    elif roman_list[i] == "L" and roman_list[i-1] == "X":
        x = x -10
        x = x + 40
    elif roman_list[i] == "C" and roman_list[i-1] == "X":
        x = x -10
        x = x + 90
    elif roman_list[i] == "D" and roman_list[i-1] == "C":
        x = x -100
        x = x + 400
    elif roman_list[i] == "M" and roman_list[i-1] == "C":
        x =x - 100
        x = x + 900
    else:
        x = x + roman_dict[roman_list[i]]

print(x)
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
