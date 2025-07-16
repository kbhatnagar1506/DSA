numbers = [2,7,11,15]
target = 9
def twosum(numbers,target):
    right = len(numbers)-1
    left = 0 
    while right>left:
        sum = numbers[left]+numbers[right]
        if sum == target:
            return[left+1,right+1]
        elif sum > target:
            right = right - 1
        elif target>sum:
            left = left + 1

print(twosum(numbers,target))
