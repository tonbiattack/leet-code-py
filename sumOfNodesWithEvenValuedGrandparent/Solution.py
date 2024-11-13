from typing import Optional

class TreeNode:
    """
    二分木のノードを表すクラス。

    Attributes:
        val (int): ノードの値
        left (Optional[TreeNode]): 左の子ノード
        right (Optional[TreeNode]): 右の子ノード
    """
    def __init__(self, val=0, left=None, right=None):
        """
        TreeNodeクラスの初期化。

        Args:
            val (int): ノードの値
            left (Optional[TreeNode]): 左の子ノード
            right (Optional[TreeNode]): 右の子ノード
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    偶数値を持つ祖父を持つノードの合計値を計算するためのクラス。
    """
    def __init__(self):
        """
        Solutionクラスの初期化。合計値の変数を初期化。
        """
        self.ans = 0  # 合計値を保持する変数

    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        """
        偶数値を持つ祖父を持つ全てのノードの値の合計を計算します。

        Args:
            root (Optional[TreeNode]): 二分木のルートノード
        
        Returns:
            int: 偶数値の祖父を持つノードの合計値
        """
        def dfs(cur: TreeNode, par: TreeNode, gra: TreeNode):
            """
            深さ優先探索（DFS）を用いてノードを探索し、偶数値の祖父を持つノードの合計を計算します。

            Args:
                cur (TreeNode): 現在のノード
                par (TreeNode): 現在のノードの親ノード
                gra (TreeNode): 現在のノードの祖父ノード
            """
            # 祖父が存在し、かつ偶数値の場合、そのノードの値を合計に加算
            if gra and gra.val % 2 == 0:
                self.ans += cur.val
            
            # 左の子ノードが存在する場合は再帰的に探索
            if cur.left:
                dfs(cur.left, cur, par)
            
            # 右の子ノードが存在する場合は再帰的に探索
            if cur.right:
                dfs(cur.right, cur, par)

        # 深さ優先探索を開始（最初は祖父も親も存在しないのでNoneを渡す）
        dfs(root, None, None)
        
        # 偶数の祖父を持つノードの合計値を返す
        return self.ans

# 呼び出し部分
if __name__ == "__main__":
    """
    二分木を手動で構築し、偶数値の祖父を持つノードの合計値を計算する。
    """
    # 二分木の構築
    root = TreeNode(6)
    root.left = TreeNode(7)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(9)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)

    # Solutionクラスのインスタンスを作成し、メソッドを呼び出す
    solution = Solution()
    result = solution.sumEvenGrandparent(root)

    # 結果を出力
    print("Sum of nodes with even-valued grandparent:", result)
