from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i,n in enumerate(nums):
            hashmap[n] = i
        
        print(hashmap)

        for i,n in enumerate(nums):
            diff = target - n
            print("diff: ", diff,"target: ", target ,"n: ", n, "i: ", i)
            if diff in hashmap and hashmap[diff] != i:
                return [i, hashmap[diff]]

nums = [3,2,4]
target = 6
solutions = Solution()
result = solutions.twoSum(nums, target)

print(result)
