/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
  let a = [];  // Use an array to store result

  for (let i = 0; i < nums.length; i++){
      for (let j = nums.length-1; j > i; j--){
          if (nums[i] + nums[j] === target){
              a.push(i);
              a.push(j);
          }
      }
  }
  return a;
};