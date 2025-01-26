"""
This is example of bit maipulation  to solve this problem

"""
from typing import List

class Solution:
    def isSubsequence(self, nums: List[int]) -> List[int]:
        x = 0
        res = []

        for num in nums:
            x = x ^ num

        k = x & (~(x-1))
        
        res1, res2 = 0,0

        for num in nums:
            if num&k !=0:
                res1=res1^num
            else:
                res2=res2^num
        
        res.append(res1)
        res.append(res2)

        return res

        
nums = [1,2,1,3,2,5]
solutions = Solution()
results = solutions.isSubsequence(nums)

print(results)