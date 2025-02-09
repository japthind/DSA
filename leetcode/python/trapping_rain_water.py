"""
    This approach has 3 possible solutions:

    Brute Force (O(n²) time, O(1) space)
        Check every element and find the water it can trap by scanning left and right.
        Very slow because it repeatedly calculates max heights for each element.
    
    Prefix & Suffix Array (O(n) time, O(n) space)
        Precompute left max and right max arrays.
        Downside: Uses extra space O(n).

    Two-Pointer Approach (O(n) time, O(1) space)
        Uses two pointers to efficiently compute trapped water.
        Best choice as it eliminates extra space usage.

    For now we can use the Two pointer solution. Maybe we can try coming up with something else later on
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height)-1
        max_l, max_r = 0,0
        water = 0

        while l<r:
            if height[l] < height[r]:
                if height[l] < max_l:
                    water += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                if height[r] < max_r:
                    water += max_r - height[r]
                else:
                    max_r = height[r]
                r -= 1
        
        return water



height = [0,1,0,2,1,0,1,3,2,1,2,1]
solutions = Solution()
results = solutions.trap(height)

print(results)