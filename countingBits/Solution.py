from typing import List

class Solution:
    """
    0 から num までの各整数のバイナリ表現に含まれる 1 のビット数を計算するクラス。
    """
    def countBits(self, num: int) -> List[int]:
        """
        与えられた整数 num に対して、0 から num までの各整数のバイナリ表現に含まれる
        1 のビット数を計算し、リストとして返します。

        Args:
            num (int): 0 から数える対象の最大の整数
        
        Returns:
            List[int]: 各整数のバイナリ表現に含まれる 1 のビット数を含むリスト
        """
        # 結果を格納するリスト。初期値として 0 をセット。
        ans = [0]
        
        # 1 から num までの数について 1 のビット数を計算する
        for i in range(1, num + 1):
            # ans[i//2] は i を 2 で割った商の 1 ビットの数、
            # i % 2 は i が奇数の場合 1 を意味し、偶数なら 0。
            ans.append(ans[i // 2] + (i % 2))
        
        # 計算結果のリストを返す
        return ans


# 呼び出し部分
if __name__ == "__main__":
    """
    テスト用の呼び出し部分。
    整数 num に対して、0 から num までの各整数のバイナリ表現に含まれる
    1 のビット数を計算して結果を出力します。
    """
    # Solution クラスのインスタンスを作成
    solution = Solution()

    # テストケースとして整数 5 を使用
    num = 5

    # メソッドを呼び出して結果を取得
    result = solution.countBits(num)

    # 結果を出力
    print(f"Number of 1-bits from 0 to {num}: {result}")
