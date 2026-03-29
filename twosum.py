class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            goal = target - num
            if goal in seen:
                return [i, seen[goal]]

            seen[num] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=list()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
                    break
        return l
        