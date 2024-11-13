# TreeNodeクラスの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ソリューションクラスの定義
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        return root

# プリオーダーでツリーを出力するヘルパーメソッド
def printPreOrder(node):
    if not node:
        return
    print(node.val, end=" ")
    printPreOrder(node.left)
    printPreOrder(node.right)

# 呼び出し部分
if __name__ == "__main__":
    # 二分探索木を手動で構築
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Solutionクラスのインスタンスを作成し、新しい値を挿入
    solution = Solution()
    new_val = 5
    updated_root = solution.insertIntoBST(root, new_val)

    # 結果をプリオーダーで表示
    print("BST after insertion (PreOrder):")
    printPreOrder(updated_root)
