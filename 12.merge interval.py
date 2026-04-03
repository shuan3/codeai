from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        print(intervals,len(intervals))
        final_arry=[]
        n=0
        while n<(len(intervals)):
            print(n)
            print(intervals[n])
            if len(intervals)==1:
                return intervals
            elif n+1!=len(intervals) and intervals[n][1]>=intervals[n+1][0] and intervals[n][1]<=intervals[n+1][1]:
                final_arry.append([intervals[n][0],intervals[n+1][1]])
                print(final_arry)
                n+=2
            elif n+1!=len(intervals) and intervals[n][1]>=intervals[n+1][0] and intervals[n][1]>intervals[n+1][1]:
                final_arry.append([intervals[n][0],intervals[n][1]])
                print(final_arry)
                n+=2
            elif n==len(intervals)-2:
                final_arry.append(intervals[n])
                final_arry.append(intervals[n+1])
                n+=2
            else:
                final_arry.append(intervals[n])
                n+=1
        return final_arry

        

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()   # sort by start time
        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            last_end = merged[-1][1]
            if last_end >= start:  # overlap
                merged[-1][1] = max(last_end, end)
            else:
                merged.append(intervals[i])
        return merged

        