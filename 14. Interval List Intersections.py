from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l=list()
        for i in range(len(firstList)):
            for j in range(len(secondList)):
                start,end=firstList[i]
                start_a,end_a=secondList[j]
                if start_a>end or start>end_a:
                    continue
                else:
#                    start_a<=end and start<=end_a:
                    l.append([max(start,start_a),min(end,end_a)])
        return l
                
        

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans