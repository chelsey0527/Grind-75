# Course Schedule
Problem can be found in [here](https://leetcode.com/problems/course-schedule/)!

### [solution](/Graph/207-CourseSchedule/solution.py)

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = { i : [] for i in range(numCourses)}
        
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # set
        visiting = set()

        def dfs(crs):
            if crs in visiting: return False
            if preMap[crs] == []: return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True
```

Time Complexity: ![O(n+p)](<https://latex.codecogs.com/svg.image?\inline&space;O(n+p)>) , Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>). Where n is courses and p is prerequisites.

