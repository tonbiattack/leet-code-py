from typing import List

class Solution:
    """
    このクラスは、与えられた配列 nums において、最初の位置から最後の位置に
    到達するために必要な最小ジャンプ回数を計算します。

    メソッド:
    jump(nums: List[int]) -> int
        与えられた配列 nums から、最小のジャンプ回数を計算し、その回数を返します。
        nums[i] は位置 i から最大で nums[i] だけ先にジャンプできることを示しています。

    アルゴリズム:
    - このアルゴリズムは貪欲法に基づいています。
    - 各ステップで、現在の範囲内 (near ~ far) でジャンプできる最も遠い位置を見つけ、次のジャンプ範囲を更新します。
    - ジャンプが成功するたびに jumps の値を1増やします。
    - far が配列の最後の要素に到達するまで繰り返します。

    パラメータ:
    nums (List[int]): ジャンプできる最大距離を表す非負整数のリスト。
    
    戻り値:
    int: 最初の位置から最後の位置に到達するための最小ジャンプ回数。
    """
    
    def jump(self, nums: List[int]) -> int:
        # 探索範囲を追跡する変数 near と far を初期化し、ジャンプ回数 jumps を初期化
        near = far = jumps = 0

        # far が配列の最後に達するまでループ
        while far < len(nums) - 1:
            farthest = 0
            # 現在の探索範囲（near から far）で到達できる最も遠い位置を探す
            for i in range(near, far + 1):
                farthest = max(farthest, i + nums[i])
            
            # 探索範囲を次のジャンプ範囲に更新
            near = far + 1
            far = farthest
            # ジャンプ回数をカウント
            jumps += 1
        
        # 最小ジャンプ回数を返す
        return jumps

if __name__ == "__main__":
    solution = Solution()

    # テストケース1: nums = [2,3,1,1,4]
    nums1 = [2, 3, 1, 1, 4]
    print(f"Minimum jumps for nums1: {solution.jump(nums1)}")  # Expected: 2

    # テストケース2: nums = [2,3,0,1,4]
    nums2 = [2, 3, 0, 1, 4]
    print(f"Minimum jumps for nums2: {solution.jump(nums2)}")  # Expected: 2
