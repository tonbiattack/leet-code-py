# 単方向リンクリストの定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # ノードの値
        self.next = next  # 次のノードへのポインタ

# Solution クラスに addTwoNumbers メソッドを実装
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # ダミーノードを作成し、結果のリンクリストを構築するための指標を作る
        dummy = ListNode()
        current = dummy
        carry = 0  # 繰り上がりのための変数

        # どちらかのリストが残っているか、繰り上がりがある間はループを回す
        while l1 or l2 or carry:
            # 現在のノードの値を取得。リストが終了していれば0を使用する
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # 2つの数値と繰り上がりを足す
            total = val1 + val2 + carry
            # 新しい繰り上がりの計算（10以上の場合、1を繰り上げる）
            carry = total // 10
            # 合計の1の位の値を次のノードとして追加
            current.next = ListNode(total % 10)
            
            # currentを次のノードに移動
            current = current.next
            # l1, l2がまだ次のノードを持っていれば進める
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # ダミーノードの次からが結果のリンクリストなので、それを返す
        return dummy.next

# ヘルパー関数: 配列を単方向リストに変換
def array_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# ヘルパー関数: 単方向リストを配列に変換して表示
def linked_list_to_array(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# main 関数
def main():
    # テスト用のリンクリストを作成
    l1 = array_to_linked_list([2, 4, 3])  # リスト: 342
    l2 = array_to_linked_list([5, 6, 4])  # リスト: 465

    # Solution クラスのインスタンスを作成し、addTwoNumbers を呼び出す
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    # 結果のリンクリストを配列に変換して表示
    print(linked_list_to_array(result))  # 出力: [7, 0, 8]  (342 + 465 = 807)

# 実行部分
if __name__ == "__main__":
    main()
