from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            print("Already at the last index. No jumps needed.")
            return 0  # No jumps needed if we are already at the last index
        
        jumps = 0  # Count of jumps made
        farthest = 0  # The farthest index we can reach
        current_end = 0  # The current boundary where we must jump

        print(f"Starting jumps computation for nums: {nums}\n")
        
        for i in range(len(nums) - 1):  # No need to check the last index
            farthest = max(farthest, i + nums[i])
            print(f"Index: {i}, Value: {nums[i]}, Farthest: {farthest}, Current End: {current_end}, Jumps: {jumps}")

            if i == current_end:  # If we reach the boundary, we must jump
                jumps += 1
                current_end = farthest
                print(f"Jumping! New Current End: {current_end}, Total Jumps: {jumps}\n")

                if current_end >= len(nums) - 1:
                    print("Reached or exceeded the last index. Stopping early.\n")
                    break  # Stop early if we can reach the last index
        
        return jumps


# Test case
solutions = Solution()
nums = [2, 3, 1, 1, 4]
result = solutions.jump(nums)

print(f"Minimum jumps required: {result}")
