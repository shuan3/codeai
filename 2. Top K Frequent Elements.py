from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dick=dict()
        l=[]
        for i in nums:
            if i not in dick:
                dick[i]=1
            else:
                dick[i]+=1
        for key,value in dick.items():
            if value>=k:
                l.append(key)
        return sorted(l)[:k]

        