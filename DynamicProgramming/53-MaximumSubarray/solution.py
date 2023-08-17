class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            # If the new number is larger than sum, replace it
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum