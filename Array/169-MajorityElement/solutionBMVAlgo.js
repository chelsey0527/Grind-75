/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  let count = 0;
  let candidate = null;

  for (let num of nums) {
    if (count === 0) {
      candidate = num; // Update the candidate when number is zero
    }

    if (num === candidate) {
      count++;
    } else {
      count--;
    }
  }

  return candidate; // After the iteration, the candidate will hold the majority element. 
};