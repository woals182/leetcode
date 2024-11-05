# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 임시헤드노드 
        head_node = ListNode(0)
        # 현재 노드를 임시헤드노드로
        current = head_node
        # 10이 넘으면 계산할 변수
        ten_change = 0

        while l1 or l2 or ten_change:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            total_val = val_l1 + val_l2 + ten_change
            
            # 합이 10이 넘으면 1 아니면 0
            ten_change = total_val // 10

            # 현재 노드 다음 노드로 연결 
            current.next = ListNode(total_val % 10)
            current = current.next

            # 다음 값으로 이동
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # 헤드 노드 이후 실제값 (임의로 0으로 주었기에)
        return head_node.next
