from typing import List
#Brute force approach: check all subarrays and count how many of them sum to k. This will have a time complexity of O(n^3) because we are checking all subarrays and calculating their sums.
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        for i in range(len(nums)):
            print(i,nums[i])
            for j in range(i,len(nums)):
                print(j,nums[j])
                if sum([ii for ii in nums[i:j+1]])==k:
                    print("yes")
                    count+=1
        return count
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum={0:1}
        total=count=0
        for i in nums:
            total+=i

            if total-k in running_sum:
                count+=running_sum[total-k]
            running_sum[total]=1+running_sum.get(total,0)
        return count
# prefix sum + hashmap
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_num = {0:1}
        total = count = 0

        for n in nums:
            total += n
            
            if total - k in sub_num:
                count += sub_num[total-k]
            
            sub_num[total] = 1 + sub_num.get(total, 0)
        
        return count
nums =[1,2,3]

print(Solution().subarraySum(nums,3))

print("yessss")
print("hey",nums[0:0])
print("hey",nums[0:1])
print("hey",nums[1:2])