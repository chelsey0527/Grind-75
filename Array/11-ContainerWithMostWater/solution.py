class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # Calculate the area between the two pointers
            # the area is the min of the left and right * numbers of bar
            area = min(height[left], height[right]) * (right - left)

            # Update the maximum area if the current area is greater
            max_area = max(max_area, area)

            # Move the pointer that corresponds to the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
            
