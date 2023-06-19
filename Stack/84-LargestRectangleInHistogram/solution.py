class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
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


# Run process
# ('3. appended stack: ', [0])

# ('1. pop ', [0], ' heights[', 0, '] >= heights[', 1, ']')
# ('3. appended stack: ', [1])

# ('2. nextSmallerLeft = ', [0, 0, 2, 0, 0, 0])
# ('3. appended stack: ', [1, 2])

# ('2. nextSmallerLeft = ', [0, 0, 2, 3, 0, 0])
# ('3. appended stack: ', [1, 2, 3])

# ('1. pop ', [1, 2, 3], ' heights[', 3, '] >= heights[', 4, ']')
# ('1. pop ', [1, 2], ' heights[', 2, '] >= heights[', 4, ']')
# ('2. nextSmallerLeft = ', [0, 0, 2, 3, 2, 0])
# ('3. appended stack: ', [1, 4])

# ('2. nextSmallerLeft = ', [0, 0, 2, 3, 2, 5])
# ('3. appended stack: ', [1, 4, 5])

# -----
# ('3. appended stack: ', [5])

# ('1. pop ', [5], ' heights[', 5, '] >= heights[', 4, ']')
# ('3. appended stack: ', [4])

# ('2. nextSmallerRight = ', [5, 5, 5, 3, 5, 5])
# ('3. appended stack: ', [4, 3])

# ('1. pop ', [4, 3], ' heights[', 3, '] >= heights[', 2, ']')
# ('2. nextSmallerRight = ', [5, 5, 3, 3, 5, 5])
# ('3. appended stack: ', [4, 2])

# ('1. pop ', [4, 2], ' heights[', 2, '] >= heights[', 1, ']')
# ('1. pop ', [4], ' heights[', 4, '] >= heights[', 1, ']')
# ('3. appended stack: ', [1])

# ('2. nextSmallerRight = ', [0, 5, 3, 3, 5, 5])
# ('3. appended stack: ', [1, 0])

# ('height: ', 2, '/ width:', 1, ' / area: ', 2, ' / res: ', 2)
# ('height: ', 1, '/ width:', 6, ' / area: ', 6, ' / res: ', 6)
# ('height: ', 5, '/ width:', 2, ' / area: ', 10, ' / res: ', 10)
# ('height: ', 6, '/ width:', 1, ' / area: ', 6, ' / res: ', 10)
# ('height: ', 2, '/ width:', 4, ' / area: ', 8, ' / res: ', 10)
# ('height: ', 3, '/ width:', 1, ' / area: ', 3, ' / res: ', 10)