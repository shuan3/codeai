from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        
        for i in range(len(nums)):
            s=1
            for j in range(len(nums)):
                if i!=j:
                    s=s*nums[j]
            l.append(s)

        return l




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
