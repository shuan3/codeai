from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hip=dict()
        for i in nums:
            hip[i]=hip.get(i,0)+1
            if hip[i]>1:
                return True
        return False
        
        



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        if len(nums_set) != len(nums):
            return True
        return False