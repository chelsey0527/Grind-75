# Partition Equal Subset Sum

Problem can be found in [here]https://leetcode.com/problems/partition-equal-subset-sum/description/)!

### [Solution](/DynamicProgramming/416-PartitionEqualSubsetSum/solution.py)

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2: return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i] == target): return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
            print('dp', dp)

        return True if target in dp else False
```

Time Complexity: ![O(n*n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n*n)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


