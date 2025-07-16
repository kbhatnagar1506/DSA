height = [1,1]
left = 0
right = len(height)-1
area = 0
width = 0
while right > left:
    width = right - left
    if height[right] > height[left]:
        bar_area = height[left]*width
    else :
        bar_area = height[right] * width

    if height[right]>height[left]:
        left = left + 1
    else:
        right = right -1
    
    if area < bar_area:
        area = bar_area
    
print(area)
    
    

    
