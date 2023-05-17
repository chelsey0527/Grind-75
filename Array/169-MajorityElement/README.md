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

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

### [solution 2 (better) ](/Array/217-ContainsDuplicate/solutionBMVAlgo.js): Boyer-Moore Voting Algorithm

```javascript
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

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

The space complexity of this improved code remains O(1) since we only use a constant amount of additional memory to store the count and candidate variables.