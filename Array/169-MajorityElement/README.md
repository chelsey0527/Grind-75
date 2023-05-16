# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/majority-element/)!

### [solution 1](/Array/169-MajorityElement//solutionSort.js): Sort

```javascript
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

<!-- ### [solution 2 ](/Array/217-ContainsDuplicate/solutionSort.js): Sort

```javascript
var containsDuplicate = function(nums) {
    nums.sort((a, b) => a - b); // sort the elements of the array in ascending order.

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] === nums[i - 1]) {
            return true; // if finding any duplicate, return true
        }
    }

    return false;
};
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>) -->