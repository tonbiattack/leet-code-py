# 二分木のノードを定義するクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノードへの参照
        self.right = right  # 右の子ノードへの参照

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # ベースケース：ノードが存在しない場合、None を返す
        if not root:
            return None
        # 再帰的に右の子ノードを反転
        right = self.invertTree(root.right)
        # 再帰的に左の子ノードを反転
        left = self.invertTree(root.left)
        # 左右の子ノードを入れ替える
        root.left = right
        root.right = left
        # 反転したノードを返す
        return root

def print_tree(node: TreeNode, level=0, label='.'):
    # 二分木を視覚的に表示するための補助関数
    if node is not None:
        print(' ' * (4 * level) + label + ':', node.val)
        print_tree(node.left, level + 1, 'L')
        print_tree(node.right, level + 1, 'R')

def main():
    # 問題の説明：
    # 与えられた二分木を左右反転（ミラーリング）させる関数を実装します。
    # これは、各ノードの左と右の子ノードを入れ替える操作を全ノードで行うことを意味します。

    # 解説：
    # この問題は、二分木を再帰的に巡回し、各ノードで左右の子ノードを入れ替えることで解決します。
    # 再帰的なアプローチにより、木の末端から順にノードを反転させていきます。

    # 例として以下の二分木を考えます：
    #
    #        4
    #      /   \
    #     2     7
    #    / \   / \
    #   1   3 6   9
    #
    # この二分木を反転すると：
    #
    #        4
    #      /   \
    #     7     2
    #    / \   / \
    #   9   6 3   1

    # 二分木を作成
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    # 反転前の二分木を表示
    print("反転前の二分木：")
    print_tree(root)

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # invertTree メソッドを呼び出して二分木を反転
    inverted_root = solution.invertTree(root)

    # 反転後の二分木を表示
    print("\n反転後の二分木：")
    print_tree(inverted_root)

if __name__ == "__main__":
    main()
