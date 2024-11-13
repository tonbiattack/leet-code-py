# TreeNodeクラスの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値
        self.left = left  # 左の子ノードへの参照
        self.right = right  # 右の子ノードへの参照

# Solutionクラスの定義
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        """
        与えられた二分探索木の最も深いレベルの全ノードの合計値を返す。

        Args:
            root (TreeNode): 二分探索木のルートノード

        Returns:
            int: 最も深いレベルのノードの値の合計
        """
        ans = {}  # 深さごとのノードの合計値を格納する辞書
        count = 0  # 現在の深さを表すカウンタ
        self.dfs(root, ans, count)

        # 最も深いレベルの合計値を返す
        return ans[max(ans)]

    def dfs(self, node, ans, count):
        """
        深さ優先探索（DFS）を用いて、各レベルのノードの値を合計する。

        Args:
            node (TreeNode): 現在のノード
            ans (dict): 深さごとのノードの合計値を保持する辞書
            count (int): 現在のノードの深さ
        """
        if node:
            # 左の子ノードが存在する場合、左側を再帰的に探索
            if node.left:
                self.dfs(node.left, ans, count + 1)
            # 右の子ノードが存在する場合、右側を再帰的に探索
            if node.right:
                self.dfs(node.right, ans, count + 1)
        # 現在の深さが辞書に存在しない場合、初期化
        if count not in ans:
            ans[count] = node.val
        else:
            ans[count] += node.val  # 既存のレベルに対して値を加算

# 呼び出し部分
if __name__ == "__main__":
    # 二分探索木を手動で構築
    # ツリー構造:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #  /         \
    # 7           8
    root = TreeNode(1)  # ルートノード
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)

    # Solutionクラスのインスタンスを作成
    solution = Solution()

    # 最も深いレベルのノードの合計値を計算
    result = solution.deepestLeavesSum(root)

    # 結果を出力
    print("Sum of deepest leaves:", result)
