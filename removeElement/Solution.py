from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
    
# テスト用コード
if __name__ == "__main__":
    solution = Solution()
    nums = [3,2,2,3]
    val = 3
    index = solution.removeElement(nums, val)
    print(index)