# TreeNodeクラスの定義
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solutionクラスの定義
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # numsリストが空ならNoneを返す（ベースケース）
        if not nums:
            return None
        # リストの中央要素を選んでその値を根ノードにする
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        # 左部分木にはリストの左半分を再帰的に処理
        root.left = self.sortedArrayToBST(nums[:mid])
        # 右部分木にはリストの右半分を再帰的に処理
        if mid < len(nums) - 1:
            root.right = self.sortedArrayToBST(nums[mid+1:])
        # 完成した二分探索木の根ノードを返す
        return root

# 呼び出し箇所
if __name__ == "__main__":
    # ソート済みの配列
    sorted_array = [-10, -3, 0, 5, 9]

    # Solutionクラスのインスタンスを作成
    sol = Solution()

    # sortedArrayToBSTメソッドを呼び出し
    bst_root = sol.sortedArrayToBST(sorted_array)

    # 結果の二分探索木を出力するためのヘルパーメソッド（オプション）
    def pre_order_traversal(node):
        if node:
            print(node.val, end=' ')
            pre_order_traversal(node.left)
            pre_order_traversal(node.right)

    # 二分探索木の前順走査で出力
    pre_order_traversal(bst_root)
