from typing import Optional

class ListNode:
    def __init__(self, val: int):
        self.val = val  # ノードの値
        self.next: Optional[ListNode] = None  # 次のノードへの参照

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 訪れたノードを保存するためのハッシュセットを初期化
        visited_nodes = set()
        while head:
            # 現在のノードがすでに訪れたノードに含まれているか確認
            if head in visited_nodes:
                # サイクルが存在するため、True を返す
                return True
            # 現在のノードを訪れたノードとして追加
            visited_nodes.add(head)
            # 次のノードに進む
            head = head.next
        # リストの終端に到達した場合、サイクルは存在しないため False を返す
        return False

def main():
    # 問題の説明：
    # 単方向リンクリストが与えられ、その中にサイクル（循環部分）が存在するかを判定します。
    # サイクルが存在するとは、リンクリストの末尾がリスト内のあるノードに再び接続していることを意味します。
    # サイクルが存在すれば True、存在しなければ False を返します。

    # 解説：
    # この問題では、リンクリストにサイクルが存在するかを効率的に検出する必要があります。
    # 一つの方法は、各ノードを巡回しながら、そのノードをハッシュセットに保存することです。
    # もし巡回中にすでに保存されたノードに再び訪れた場合、サイクルが存在することになります。
    # この方法は O(n) の時間計算量と O(n) の空間計算量を持ちます。

    # ノードを作成してリンクリストを構築

    # テストケース 1: サイクルが存在しない場合
    # リンクリスト: 1 -> 2 -> 3 -> 4 -> None
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    # テストケース 2: サイクルが存在する場合
    # リンクリスト: 1 -> 2 -> 3 -> 4
    #                      ^         |
    #                      |_________|
    node5 = ListNode(1)
    node6 = ListNode(2)
    node7 = ListNode(3)
    node8 = ListNode(4)

    node5.next = node6
    node6.next = node7
    node7.next = node8
    node8.next = node6  # サイクルを形成

    # Solution クラスのインスタンスを作成
    solution = Solution()

    # テストケース 1 を検証
    result1 = solution.hasCycle(node1)
    print("テストケース 1 - サイクルが存在しない場合の結果:", result1)  # 期待される出力: False

    # テストケース 2 を検証
    result2 = solution.hasCycle(node5)
    print("テストケース 2 - サイクルが存在する場合の結果:", result2)  # 期待される出力: True

if __name__ == "__main__":
    main()
