from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 配列の長さを取得
        n = len(nums)

        # k を n で割った余りに変換して、無駄な回転を除去
        k = k % n

        # 回転後の要素を一時的に格納する配列を用意
        rotated = [0] * n

        # 配列の各要素を回転させて新しい位置に移動
        for i in range(n):
            # (i + k) % n の解説
            #
            # i は元の配列 nums における現在のインデックスを示します。
            # k は右に回転させる回数を表します。
            # n は配列 nums の全長です。
            #
            # たとえば、配列の要素を右に k 回回転させる場合、
            # 新しい位置は「元の位置 i に k を足した値」が新しいインデックスになります。
            # しかし、配列の長さを超えると要素がループする必要があるため、
            # 配列の長さ n で割った余り (mod演算) を使って、新しい位置を計算します。
            rotated[(i + k) % n] = nums[i]

        # 元の配列に新しい順序を上書き
        for i in range(n):
            nums[i] = rotated[i]


# 呼び出し例
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"Before rotation: {nums}")

    # 配列を k 回転させる
    Solution().rotate(nums, k)

    print(f"After rotation: {nums}")
