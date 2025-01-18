from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_arr = []
        suffix_arr = []
        result_arr = []

        prefix = 1
        suffix = 1

        for i in range(len(nums)):
            prefix *= nums[i]
            prefix_arr.append(prefix)
        
        print(prefix_arr)

        for i in range((len(nums)-1), -1, -1):
            suffix *= nums[i]
            suffix_arr.insert(0,suffix)
        
        print("suffix", suffix_arr)

        for i in range(len(nums)):
            if i == 0:
                print("if", i)
                result_arr.insert(i,1 * suffix_arr[i+1])
            elif i == len(nums)-1:
                print("elif", i)
                result_arr.insert(i, prefix_arr[i-1] * 1)
            else:
                print(i)
                result_arr.insert(i, prefix_arr[i-1] * suffix_arr[i+1])
        
        print(result_arr)


nums = [1,2,3]
solutions = Solution()
result = solutions.productExceptSelf(nums)

