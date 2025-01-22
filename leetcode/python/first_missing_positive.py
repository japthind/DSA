"""
    https://leetcode.com/problems/first-missing-positive/description/

    First we will try the brute force approach
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        result = None
        if max(nums) < 0:
            result = 1
        for i in range(max(nums)):
            if i not in nums:
                if i != 0:
                    result = i
                    break
        if result == None:
            result = max(nums)+1
        return result           


nums = [-5]
solutions = Solution()
result = solutions.firstMissingPositive(nums)

print(result)


"""
    using hashset

    The below approach uses the Hashset to store the nums list as set as a O(1) lookup time

    Time Complexity = O(n)
    Space Complexity = O(n)
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hashset = set()
        result = None

        for num in nums:
            hashset.add(num)      

        print(hashset)

        if max(hashset) < 0:
            result = 1
            return result

        for i in range(len(nums)+1):
            if i not in hashset and i != 0:
                result = i 
                break
        
        if result == None:
            result = max(hashset) + 1
            return result
        else:
            return result


nums = [2]
solutions = Solution()
result = solutions.firstMissingPositive(nums)

print(result)


"""
    There can be a third approach to use which is using Cycle Sort.
    
    Come back to this later and figure this out
"""