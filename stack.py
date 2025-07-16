def isValidParentheses(s: str):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            # In case of any invalid characters
            return False
        return True
print(isValidParentheses("()[]"))




# Given an array of integers, write a function that returns an array such that for each index i, it contains the next greater element to the right of arr[i]. If none exists, put -1.

# Example:
# Input: [4, 5, 2, 25]
# Output: [5, 25, 25, -1]

# Function Signature:
# def nextGreaterElements(nums: List[int]) -> List[int]

input = [4,5,2,25]
stack = []
for i in input:
    stack.insert(0,i)
for i in 