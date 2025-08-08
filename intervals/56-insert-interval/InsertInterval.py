class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i, n = 0,len(intervals)
        # Adding intervals less than the newInterval into result
        while i< n and intervals[i][1]<newInterval[0]:
            result.append(intervals[i])
            i+=1
        # Merging the overlapping intervals
        while i<n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i+=1
        result.append(newInterval)
        while i<n:
            result.append(intervals[i])
            i+=1
        return result