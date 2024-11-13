from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        # 2ステップずつ進むループ
        for i in range(0, len(nums), 2):
            # nums[i] 回 nums[i+1] を繰り返して ans に追加
            ans += [nums[i + 1]] * nums[i]
        return ans


if __name__ == "__main__":
    solution = Solution()

    # サンプル入力
    nums = [1, 2, 3, 4]

    # デコードされたリストを作成して結果を出力
    decompressed_list = solution.decompressRLElist(nums)
    print("Decompressed List:", decompressed_list)  # [2, 4, 4, 4]
