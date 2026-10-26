class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        result = []
        for interval in intervals:
            if interval[1] < new_start:
                result.append(interval)
            elif interval[0] > new_end:
                result.append([new_start, new_end])
                new_start, new_end = interval
            else:
                new_start = min(interval[0], new_start)
                new_end = max(interval[1], new_end)
            
        result.append([new_start, new_end])
        return result
        
        