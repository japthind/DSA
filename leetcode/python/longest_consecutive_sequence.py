from typing import List
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        count = 0

        for num in numset:
            if (num - 1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                
                count = max(length, count)
        
        return count


nums = [100,4,200,1,3,2]
solutions = Solution()
result = solutions.longestConsecutive(nums)

print(result)