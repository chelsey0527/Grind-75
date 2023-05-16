/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
  
  // Sort before find
  nums.sort((a, b) => a - b); 

  if ( nums.length > 1){
    // Since the number of the element will excess n/2 we can directly get the median
    return nums[Math.ceil( nums.length/2)-1];
  } else {
    return nums[0];
  }
 
};