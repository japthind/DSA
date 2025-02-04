"""
   Brute Force Approach with O(n^2) time complexity
"""

from typing import List

# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         res = 0

#         for i in range(len(height)):
#             for j in range(1, len(height)):
#                 area = (j - i) * min(height[i], height[j])
#                 res = max(res, area)

#         return res


# height = [1,8,6,2,5,4,8,3,7]
# solutions = Solution()
# result = solutions.maxArea(height)

# print(result)

"""
    O(n) Solution
    This is using the Two pointer Solution
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        l,r = 0, len(height)-1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res


height = [1,8,6,2,5,4,8,3,7]
solutions = Solution()
result = solutions.maxArea(height)

print(result)
