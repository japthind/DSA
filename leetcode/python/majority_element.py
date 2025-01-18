"""
    The below code is brute force approach to solve this problem

    Time complexity: O(n^2) as there are 2 loops which run for n number of times

    This approach works fine for small test cases but for large number of inputs it is not optimized.
"""

from typing import List

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         sum = 0
#         largest_element = 0

#         for i in range(len(nums)):
#             count = 0
#             for j in range(len(nums)):
#                 if nums[i] == nums[j]:
#                     count += 1
#             if count > sum:
#                 sum = count
#                 largest_element = nums[i]
        
#         return largest_element
        
# nums = [1,2,3,4,5,1,2,3,2,3,3]
# solutions = Solution()
# result = solutions.majorityElement(nums)

# print(result)

# ***********************************************************************************************************************************************

"""
    The below approach uses the logic that if the majority element is the element that appears more than ⌊n / 2⌋ times.
    Otherwise this approach wont work.

    The idea is that if a number appears more than n//2 times it will surely be present at the middle index.
"""

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[len(nums) // 2]
        
# nums = [3,2,3]
# solutions = Solution()
# result = solutions.majorityElement(nums)

# print(result)

# ***********************************************************************************************************************************************

"""
    Boyer-Moore Voting Algorithm

    Here what we do is that we just traverse the array once
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        largest_element = 0

        for num in nums:
            if count == 0:
                largest_element = num
            count += (1 if largest_element == num else -1)

        return largest_element
        
nums = [3,2,3]
solutions = Solution()
result = solutions.majorityElement(nums)

print(result)