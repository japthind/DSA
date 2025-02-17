from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for n in nums:
            dict[n] = 1 + dict.get(n,0)

        print("**", dict)

        s = list(dict.values())

        s.sort(reverse=True)
        x= s[:k]
        print(x)
        l = []
        for i in x:
            print("i", i)
            for j in dict.keys():
                print("j", j)
                if dict[j] == i and j not in l:
                    l.append(j)
                print("l", l)
        
        return l

solutions = Solution()
nums = [1,2]
k = 2

result = solutions.topKFrequent(nums, k)

print(result)