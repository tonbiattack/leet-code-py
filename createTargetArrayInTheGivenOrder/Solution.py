from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i],nums[i])
        return target
    
if __name__ == "__main__":
    solution = Solution()

    # サンプル入力
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]

    # ターゲット配列を作成して結果を出力
    target_array = solution.createTargetArray(nums, index)
    print("Target Array:", target_array)  # [0, 4, 1, 3, 2]
    

