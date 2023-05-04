/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const map = new Map(); // use map to store visted numbers

    for( let i = 0; i < nums.length; i++){
        if (!map.has(nums[i])) {
            map.set(nums[i], i);
        } else {
            return true; // if finding any duplicate, return true
        }
    }

    return false; 
};