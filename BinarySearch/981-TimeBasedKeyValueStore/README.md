# Time Based Key-Value Store
Problem can be found in [here](https://leetcode.com/problems/time-based-key-value-store/description/)!

### [Solution](/BinarySearch/981-TimeBasedKeyValueStore/solution.py)

```python
class TimeMap:

    def __init__(self):
        self.store = {} #key : list of [value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store: 
            self.store[key] = []
        self.store[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # Binary Search
        l, r = 0 , len(values) - 1

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
                # Invalid value, so we dont set
                

        return res
```

Time Complexity: ![O(logn)](<https://latex.codecogs.com/svg.image?\inline&space;O(logn)>), Space Complexity: ![O(n)](<https://latex.codecogs.com/svg.image?\inline&space;O(n)>)


