from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for str in strs:
            sorted_word = ''.join(sorted(str))
            hashmap[sorted_word].append(str)

        return list(hashmap.values())
                



strs = ["eat","tea","tan","ate","nat","bat"]
solutions = Solution()
result = solutions.groupAnagrams(strs)

print(result)