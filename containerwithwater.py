height = [2,2,2]
areas = []
n = len(height)
x = 0
while x < n-1: #7
    rightcursor = n-1
    for leftcursor in range(0,n): #7 2n
        if height[rightcursor] > height[leftcursor] :
            min_height = height[leftcursor]
        elif height[leftcursor] > height[rightcursor]:
            min_height = height[rightcursor]
        else:
            min_height = height[leftcursor]
        area = min_height*(rightcursor-leftcursor)
        areas.append(area)
        x = x + 1
print(max(areas))