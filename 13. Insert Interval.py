
from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals=sorted(intervals)
        l=[intervals[0]]
        for i in range(1,len(intervals)):
            start,end=intervals[i]
            if start>=l[-1][0] and start<=l[-1][1] and end>l[-1][1]:
                l[-1][1]=end
            elif start>=l[-1][0] and start<=l[-1][1] and end<=l[-1][1]:
                pass
            else:
                l.append(intervals[i])
        return l

        