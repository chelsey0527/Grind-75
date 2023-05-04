/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
  nums.sort((a, b) => a - b); // sort the elements of the array in ascending order.

  for (let i = 1; i < nums.length; i++) {
      if (nums[i] === nums[i - 1]) {
          return true; // if finding any duplicate, return true
      }
  }

  return false;
};