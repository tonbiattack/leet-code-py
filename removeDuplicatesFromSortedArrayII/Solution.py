class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

# テスト用コード
if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,3]
    new_length = solution.removeDuplicates(nums)

    print("New length:", new_length)
    print("Modified array:", nums[:new_length])
