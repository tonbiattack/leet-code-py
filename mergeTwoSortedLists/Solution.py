# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # ダミーノードを作成しておき、ここから新しいリストを構築する
        dummy = ListNode()
        current = dummy
        
        # 両方のリストを走査しながらマージする
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 残っているリストを追加する
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        # 最初のダミーノードを飛ばして、マージされたリストを返す
        return dummy.next

# テスト用のリスト作成関数
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# テスト用のリスト表示関数
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# テスト用コード
if __name__ == "__main__":
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    
    solution = Solution()
    merged_list = solution.mergeTwoLists(list1, list2)
    
    print("Merged Linked List:")
    print_linked_list(merged_list)
