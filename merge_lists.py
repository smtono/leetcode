from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: List[ListNode], list2: List[ListNode]) -> List[ListNode]:
    answer = []
    sorted = False
    head1 = list1[0]
    head2 = list2[0]

    while not sorted:
        if (head1.val < head2.val):
            answer.append(head1)
            if head1.next:
                head1 = head1.next
            elif head2.next:
                answer.append(head2.next)
        else:
            answer.append(head2)
            if head2.next:
                head2 = head2.next
    return answer[0]

list1 = [ListNode(0), ListNode(2), ListNode(4)]
list2 = [ListNode(1), ListNode(3), ListNode(5)]
print(mergeTwoLists(list1, list2))