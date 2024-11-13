# 必要な型アノテーションのインポート
from typing import List

# Solution クラスに maxSubArray メソッドを実装
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 一時的に部分配列の和を保持する変数
        temp = 0
        # 最大の要素を初期値とする
        max_num = max(nums)
        
        # 配列内の全要素に対してループ処理
        for i in range(len(nums)):
            # 現在の要素を部分配列の和に加算
            temp += nums[i]
            
            # 現在の部分配列の和が正の場合、最大値と比較して更新
            if temp >= 0:
                max_num = max(max_num, temp)
            else:
                # 部分配列の和が負になったら、リセット
                temp = 0
        
        # 最大部分配列の和を返す
        return max_num

# ヘルパー関数：配列と結果を出力する
def test_max_sub_array():
    # テストケースの定義
    test_cases = [
        [-2,1,-3,4,-1,2,1,-5,4],  # 連続する部分配列 [4,-1,2,1] の和は 6
        [1],  # 要素1つの場合、そのまま最大和
        [5,4,-1,7,8],  # 連続する部分配列 [5,4,-1,7,8] の和は 23
        [-1,-2,-3,-4],  # 全て負の数の場合、最大の単一要素を選ぶ
    ]

    # 各テストケースに対して、maxSubArray を呼び出し、結果を表示する
    solution = Solution()
    for nums in test_cases:
        print(f"Input: {nums}")
        result = solution.maxSubArray(nums)
        print(f"Maximum Subarray Sum: {result}\n")

# テスト関数を実行
test_max_sub_array()
