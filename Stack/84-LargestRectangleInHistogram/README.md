# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/largest-rectangle-in-histogram/)!

### [solution](/Stack/84-LargestRectangleInHistogram/)

```python
class Solution(object):
    def largestRectangleArea(self, heights):

        n = len(heights)  # Get the length of the heights list
        
        # left boundary => next smaller element to the left
        stack = []  # Initialize an empty stack
        nextSmallerLeft = [0] * n  # Initialize a list to store the indices of next smaller elements to the left
        
        # Calculate the next smaller element to the left for each element in heights
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()  # Remove elements from the stack that are greater than or equal to the current element
            if stack:
                nextSmallerLeft[i] = stack[-1] + 1  # Store the index of the next smaller element to the left
            stack.append(i)  # Push the current element's index to the stack
        
        # right boundary => next smaller element to the right
        stack = []  # Reset the stack
        nextSmallerRight = [n - 1] * n  # Initialize a list to store the indices of next smaller elements to the right
        
        # Calculate the next smaller element to the right for each element in heights
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()  # Remove elements from the stack that are greater than or equal to the current element
            if stack:
                nextSmallerRight[i] = stack[-1] - 1  # Store the index of the next smaller element to the right
            stack.append(i)  # Push the current element's index to the stack
        
        res = heights[0]  # Initialize the result with the height of the first
        for i in range(n):
            height = heights[i] 
            width = nextSmallerRight[i] - nextSmallerLeft[i] + 1  
            area = height * width  # Calculate the area of the current rectangle
            res = max(res, area)  # Update the result if the current area is larger than the previous maximum
            print('height:', height, '/ width:', width, '/ area:', area, '/ res:', res)
            
        return res
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) for each