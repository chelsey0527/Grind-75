class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        red_ptr = 0
        blue_ptr = len(nums) - 1
        current_ptr = 0

        while current_ptr <= blue_ptr:
            if nums[current_ptr] == 0:
                nums[current_ptr], nums[red_ptr] = nums[red_ptr], nums[current_ptr]
                red_ptr += 1
                current_ptr += 1
            elif nums[current_ptr] == 2:
                nums[current_ptr], nums[blue_ptr] = nums[blue_ptr], nums[current_ptr]
                blue_ptr -= 1
            else:
                current_ptr += 1
