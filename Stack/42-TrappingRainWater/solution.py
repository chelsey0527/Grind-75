class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int                                       
        """
        
        # Find the max from each side
        left_max, right_max = 0, 0
        # Store the pointers' position
        l, r = 0, len(height) - 1
        # Store the answer
        ans = 0

        while l < r:
            if height[l] < height[r]:
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    ans += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    ans += right_max - height[r]
                r -= 1
        
        return ans