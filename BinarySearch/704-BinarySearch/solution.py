class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        for i in range(len(nums)//2+1):
            if nums[i] == target: return i
            if nums[len(nums) - 1 - i] == target: return len(nums) - 1 - i

        return -1