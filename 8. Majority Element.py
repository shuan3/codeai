from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m=len(nums)/2
        d=dict()
        l=set()
        
        for i in nums:
            d[i]=d.get(i,0)+1
            if d[i]>=m:
                l.add(i)
        return max(l)






# standard solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        nums=sorted(nums)
        print(len(nums)//2)
        return nums[len(nums)//2]