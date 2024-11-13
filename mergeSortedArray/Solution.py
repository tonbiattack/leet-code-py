# Solutionクラスの定義
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # nums2の要素をnums1の空き部分にコピー
        for j in range(n):
            nums1[m+j] = nums2[j]
        # 結合したnums1をソートして最終結果を作成
        nums1.sort()

# 呼び出し箇所
if __name__ == "__main__":
    # 2つのソート済み配列を用意
    nums1 = [1, 2, 3, 0, 0, 0]  # nums1には m=3 の要素と、残りの0はnums2の要素を入れるための空き領域
    m = 3  # nums1の有効な要素の数
    nums2 = [2, 5, 6]  # nums2にはソートされた別の配列
    n = 3  # nums2の要素の数

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # mergeメソッドの呼び出し
    sol.merge(nums1, m, nums2, n)

    # 結果の出力
    print(f"Merged array: {nums1}")
