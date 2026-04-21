# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # prevSeen = set()
        # currNode = head
        # while currNode:
        #     if currNode in prevSeen:
        #         return True
        #     prevSeen.add(currNode)
        #     currNode = currNode.next
        # return False

        # ^ Solution Time Complx: O(n), Space Complx: O(n)
        # v Solution Time Complx: O(n), Space Complx: O(1)

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False