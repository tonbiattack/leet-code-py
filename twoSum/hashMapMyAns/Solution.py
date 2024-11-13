from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        # Find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [i, numMap[complement]]
            else:
                numMap[nums[i]] = i

        return []  # No solution found

# 例としての呼び出し
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print(f"Indices of the two numbers that add up to {target}: {result}")
