# Contains Duplicate

Problem can be found in [here](https://leetcode.com/problems/3sum/)!

### [solution 1](/Array/15-3Sum/solution.js): Brute force 

```javascript
var threeSum = function(nums) {
  nums.sort((a, b) => a - b);
  let ans = [];

  for (let i = 0; i < nums.length - 2; i++) {
      // Skip duplicates for the first element
      if (i > 0 && nums[i] === nums[i - 1]) {
          continue;
      }

      // Left pointer represents the next number
      let left = i + 1;
      // Right pointer represents the last number
      let right = nums.length - 1;

      while (left < right) {
          let sum = nums[i] + nums[left] + nums[right];

          if (sum === 0) {
              // Push the array into the answer array
              ans.push([nums[i], nums[left], nums[right]]);

              // Skip duplicates for the second element
              while (left < right && nums[left] === nums[left + 1]) {
                  left++;
              }

              // Skip duplicates for the third element
              while (left < right && nums[right] === nums[right - 1]) {
                  right--;
              }

              left++;
              right--;
          // If its too small, move left forward 
          } else if (sum < 0) {
              left++;
          // If its too large, move right back
          } else {
              right--;
          }
      }
  }

  return ans;
};

```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
This does not meet the requirement "Time Complexity must not exceed O(n)".


### [solution 2](/Array/15-3Sum/betterSolution.js): Prefix and Sufix

```javascript
var threeSum = function(nums) {
  nums.sort((a, b) => a - b);
  let ans = [];

  for (let i = 0; i < nums.length - 2; i++) {
      // Skip duplicates for the first element
      if (i > 0 && nums[i] === nums[i - 1]) {
          continue;
      }

      // Left pointer represents the next number
      let left = i + 1;
      // Right pointer represents the last number
      let right = nums.length - 1;

      while (left < right) {
          let sum = nums[i] + nums[left] + nums[right];

          if (sum === 0) {
              // Push the array into the answer array
              ans.push([nums[i], nums[left], nums[right]]);

              // Skip duplicates for the second element
              while (left < right && nums[left] === nums[left + 1]) {
                  left++;
              }

              // Skip duplicates for the third element
              while (left < right && nums[right] === nums[right - 1]) {
                  right--;
              }

              left++;
              right--;
          // If its too small, move left forward 
          } else if (sum < 0) {
              left++;
          // If its too large, move right back
          } else {
              right--;
          }
      }
  }

  return ans;
};

```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

In this method, we seperate prefix and sufix to calculate their product seperately. And we calculate their product and store in the result array.