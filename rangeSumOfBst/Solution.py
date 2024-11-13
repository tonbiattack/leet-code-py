class TreeNode:
    """
    二分探索木 (Binary Search Tree) のノードを表すクラス。
    ノードは整数の値 val、左の子ノード left、右の子ノード right を持つ。
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val   # ノードの値
        self.left = left   # 左の子ノード
        self.right = right   # 右の子ノード


class Solution:
    """
    与えられた二分探索木 (BST) のノード値が、指定された範囲 [L, R] の間にあるノードの値の合計を計算するクラス。
    """

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        """
        二分探索木の中で、指定された範囲 [L, R] に含まれるノードの値の合計を返すメソッド。

        Parameters:
        root (TreeNode): 二分探索木のルートノード
        L (int): 範囲の最小値
        R (int): 範囲の最大値

        Returns:
        int: 範囲 [L, R] に含まれるノードの値の合計
        """
        def dfs(node):
            """
            深さ優先探索 (DFS) を使用して、ツリーのノードを再帰的に探索する内部メソッド。
            範囲 [L, R] に含まれるノードの値を見つけ、合計に加算する。

            Parameters:
            node (TreeNode): 現在のノード
            """
            if node:
                # 現在のノードの値が範囲 [L, R] に含まれている場合、その値を合計に加算
                if L <= node.val <= R:
                    self.ans += node.val
                
                # 現在のノードの値が L より大きい場合、左部分木を探索する。
                # これは左のノードに範囲 [L, R] に含まれる値がある可能性があるため。
                if L < node.val:
                    dfs(node.left)

                # 現在のノードの値が R より小さい場合、右部分木を探索する。
                # これは右のノードに範囲 [L, R] に含まれる値がある可能性があるため。
                if R > node.val:
                    dfs(node.right)

        self.ans = 0  # 範囲 [L, R] に含まれる値の合計を保持する変数を初期化
        dfs(root)     # ルートノードから探索を開始
        return self.ans  # 計算した合計を返す


# 呼び出し部分
if __name__ == "__main__":
    # 二分探索木の構築
    # ツリー構造:
    #         10
    #        /  \
    #       5   15
    #      / \    \
    #     3   7   18
    root = TreeNode(10)              # ルートノード
    root.left = TreeNode(5)          # 左の子ノード
    root.right = TreeNode(15)        # 右の子ノード
    root.left.left = TreeNode(3)     # 5 の左の子ノード
    root.left.right = TreeNode(7)    # 5 の右の子ノード
    root.right.right = TreeNode(18)  # 15 の右の子ノード

    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # 範囲 [L, R] の設定
    L, R = 7, 15  # 範囲 [7, 15]

    # 範囲内の値の合計を計算して結果を返す
    result = solution.rangeSumBST(root, L, R)

    # 計算結果の出力
    # 出力: Sum of values in range [7, 15] is: 32
    print("Sum of values in range [", L, ",", R, "] is:", result)
