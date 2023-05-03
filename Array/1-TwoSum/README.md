# Two Sum

Problem can be found in [here](https://leetcode.com/problems/two-sum/)!

### [Solution](/Array/1-TwoSum/solution.js): Brute Force

```javascript
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
```

Time Complexity: ![O(n^2)](<https://latex.codecogs.com/svg.image?\inline&space;O(n^2)>), Space Complexity: ![O(1)](<https://latex.codecogs.com/svg.image?\inline&space;O(1)>)

Explanation: Simply iterate the array and find the target value among the array in each iteration.

### [Improved Solution](/Array/1-TwoSum/betterSolution.js): Map

```javascript
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
```

Time Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)

