# K Cloest Pointes to Origin

Problem can be found in [here](https://leetcode.com/problems/k-closest-points-to-origin/description/)!

### [solution](/Heap/973-KClosestPointstoOrigin/solution.py)

```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        pts = []
        for x, y in points:
            dist = (abs(x - 0) ** 2) + (abs(y-0) ** 2)
            pts.append([dist, x, y])
        
        res = []
        heapq.heapify(pts)
        for i in range(k):
            dist, x, y = heapq.heappop(pts)
            res.append([x, y])
        return res     
```

Time Complexity: ![O(nlogn)](<https://latex.codecogs.com/svg.image?\inline&space;O(nlogn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)
