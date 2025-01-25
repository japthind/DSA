"""
    Brute Force Approach

    Time Complexity: O(nlogn)
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List:
        res = []

        for i in range(n+1):
            result = 0
            while(i>0):
                if(i%2) == 1:
                    result +=1
                i=i//2
            res.append(result)
        
        return res
    
n = 2
solutions = Solution()
result = solutions.countBits(n)

print(result)