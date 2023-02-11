from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> List[ListNode]:
    answer = []
    sorted = False
    head1 = list1[0]
    head2 = list2[0]

    while not sorted:
        if head1 == None or head2 == None: # there is no comparison to make
            if head1: # if value from first list exist, add it
                answer.append(head1) 
                if head1.next: # traverse to next item if it exists
                    head1 = head1.next
                else: # now this list is done
                    head1 = None
            elif head2:
                answer.append(head2)
                if head2.next: # traverse to next item if it exists
                    head2 = head2.next
                else: # now this list is done
                    head2 = None
            else: # it must be sorted
                sorted = True
        elif (head1.val <= head2.val): # pick one from first list
            answer.append(head1) # add to sorted list
            if head1.next: # if next exist, traverse
                head1 = head1.next
            else:
                head1 = None
        else: # pick one from second list
            answer.append(head2)
            if head2.next:
                head2 = head2.next
            else:
                head2 = None
        
    # Now must connect the nodes in list to each other
    i = 1
    for node in answer:
        if node.next:
            node.next = answer[i]
            i += 1
        else:
            node.next = None
            
    return answer[0]

list1 = [ListNode(0), ListNode(2), ListNode(4)]
list1[0].next = list1[1]
list1[1].next = list1[2]

list2 = [ListNode(1), ListNode(3), ListNode(4), ListNode(5)]
list2[0].next = list2[1]
list2[1].next = list2[2]
list2[2].next = list2[3]

print(mergeTwoLists(list1, list2))