# TreeNodeクラスの定義
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

# Solutionクラスの定義
class Solution:
    """
    二つの二分木をマージするためのクラス。
    """
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        二つの二分木 t1 と t2 をマージし、新しい二分木を返します。

        各ノードに対して、t1 と t2 の対応するノードの値を足し合わせて新しいノードを作成します。
        一方が None の場合は、もう一方のノードをそのまま使用します。

        Args:
            t1 (TreeNode): 最初の二分木のルートノード
            t2 (TreeNode): 二番目の二分木のルートノード
        
        Returns:
            TreeNode: マージされた新しい二分木のルートノード
        """
        if not t1 and not t2:
            return None  # 両方がNoneの場合は新しいノードは作成せずNoneを返す
        if not t1:
            return t2  # t1がNoneの場合、t2のノードをそのまま返す
        if not t2:
            return t1  # t2がNoneの場合、t1のノードをそのまま返す
        
        # t1とt2の両方が存在する場合、それぞれの値を足し合わせた新しいノードを作成
        ans = TreeNode(t1.val + t2.val)
        # 左部分木を再帰的にマージ
        ans.left = self.mergeTrees(t1.left, t2.left)
        # 右部分木を再帰的にマージ
        ans.right = self.mergeTrees(t1.right, t2.right)
        return ans  # マージされたノードを返す

# 呼び出し部分
if __name__ == "__main__":
    """
    二分木を手動で構築し、二つの木をマージして結果を表示する。
    """
    # 最初の二分木を手動で構築
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    # 二番目の二分木を手動で構築
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    # Solutionクラスのインスタンスを作成し、メソッドを呼び出す
    solution = Solution()
    result = solution.mergeTrees(t1, t2)

    # 二分木をプリオーダー（先行順）で出力する関数
    def printTree(node):
        if node:
            print(node.val, end=' ')  # 現在のノードの値を出力
            printTree(node.left)  # 左部分木を再帰的に出力
            printTree(node.right)  # 右部分木を再帰的に出力

    # マージ後の二分木を出力
    print("Merged tree in preorder:")
    printTree(result)
