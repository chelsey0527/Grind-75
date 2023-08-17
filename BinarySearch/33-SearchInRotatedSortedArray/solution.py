class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2


            if nums[mid] == target:
                return mid

            # Check if left half is sorted
            if nums[left] <= nums[mid]:
                
                # If target is between left and mid
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # Else, move to left to mid + 1
                else:
                    left = mid + 1
            # Otherwise, right half is sorted
            else:
                # If target is between mid and right
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # Else, move right to mid - 1
                else:
                    right = mid - 1

        return -1