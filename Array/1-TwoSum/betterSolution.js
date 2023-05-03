/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
  let map = new Map(); // use map to store result
  
  for (let i = 0; i < nums.length; i++) {
      let diff = target - nums[i];
      
      // check if previous value contains diff
      if (map.has(diff)) {
          return [i, map.get(diff)];
      }
      
      // if not diff, store the value.
      map.set(nums[i], i);
  }
};