
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

        



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                return res + intervals[i:]
            elif intervals[i][1] < newInterval[0]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res