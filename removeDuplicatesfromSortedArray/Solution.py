class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        unique_index = 1  # 次のユニークな要素を置く場所

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_index] = nums[i]
                unique_index += 1

        return unique_index

# テスト用コード
if __name__ == "__main__":
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    new_length = solution.removeDuplicates(nums)

    print("New length:", new_length)
    print("Modified array:", nums[:new_length])
