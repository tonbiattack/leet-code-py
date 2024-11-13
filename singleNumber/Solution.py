from typing import List

class Solution:
    """
    一つだけ異なる回数（1回）出現する要素を見つけるためのクラス。
    """
    def singleNumber(self, nums: List[int]) -> int:
        """
        配列内で一度だけ出現する要素を探します。
        他の要素はすべて2回出現します。

        XOR演算を使うことで、重複する要素を効率的に取り除き、一つだけ出現する要素を見つけることができます。

        Args:
            nums (List[int]): 整数のリスト

        Returns:
            int: 一度だけ出現する要素
        """
        ans = 0  # XOR結果を格納する変数

        # 配列内のすべての数に対してXOR演算を行う
        for n in nums:
            ans ^= n  # XOR演算: 同じ数をXORするとキャンセルされ、異なる数が残る
        
        return ans  # 最終的に一度だけ出現する数がansに残る


# 呼び出し部分
if __name__ == "__main__":
    """
    テスト用の呼び出し部分です。
    配列内で一度だけ出現する要素を見つけます。
    """
    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # テスト用のリスト
    nums = [4, 1, 2, 1, 2]

    # メソッドを呼び出して結果を取得
    result = solution.singleNumber(nums)

    # 結果を表示
    print("The single number is:", result)
