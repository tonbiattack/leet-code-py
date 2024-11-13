from typing import Optional


class TreeNode:
    """
    TreeNodeはバイナリツリーの各ノードを表します。

    属性:
    - val (int): ノードの値
    - left (Optional[TreeNode]): 左の子ノード
    - right (Optional[TreeNode]): 右の子ノード
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solutionクラスは、与えられたバイナリツリーの最小深度を計算するためのメソッドを提供します。

    メソッド:
    minDepth(root: Optional[TreeNode]) -> int
        与えられたバイナリツリーの最小深度を、深さ優先探索 (DFS) を用いて計算します。

    アルゴリズムの流れ:
    1. ルートがNoneの場合、深さは0として処理します。
    2. 片方の子ノードが存在しない場合、もう片方の子ノードの深度を計算します。
    3. 両方の子ノードが存在する場合は、左右の子ノードの深さの最小値に1を加えます。

    パラメータ:
    root (Optional[TreeNode]): バイナリツリーのルートノード

    戻り値:
    int: バイナリツリーの最小深度
    """

    # DFSによる最小深度の計算
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
#         左右の子ノードがある場合、左右の最小の深さを選びます。
# 片方の子ノードしかない場合は、もう片方の深さを基に計算します。
        if None in [root.left, root.right]:
            return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


# 呼び出しコード例
if __name__ == "__main__":
    solution = Solution()

    # テストケース1: root = [3,9,20,None,None,15,7]
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    # Expected: 2
    print(f"Minimum depth for root1: {solution.minDepth(root1)}")

    # テストケース2: root = [2,None,3,None,4,None,5,None,6]
    root2 = TreeNode(2)
    root2.right = TreeNode(3)
    root2.right.right = TreeNode(4)
    root2.right.right.right = TreeNode(5)
    root2.right.right.right.right = TreeNode(6)
    # Expected: 5
    print(f"Minimum depth for root2: {solution.minDepth(root2)}")

    # テストケース3: root = []
    root3 = None
    # Expected: 0
    print(f"Minimum depth for root3: {solution.minDepth(root3)}")
