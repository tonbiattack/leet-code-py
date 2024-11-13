from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# テスト用コード
if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    new_length = solution.removeDuplicates(nums)

    print("New length:", new_length)
    print("Modified array:", nums[:new_length])
