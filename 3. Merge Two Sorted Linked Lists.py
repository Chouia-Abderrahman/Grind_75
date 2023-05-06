class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # create a dummy node to start the merged list
    dummy = ListNode(0)
    # create a pointer to keep track of the current node in the merged list
    current = dummy

    # loop until we reach the end of one of the lists
    while l1 and l2:
        # compare the values of the current nodes in the two lists
        if l1.val < l2.val:
            # add the current node from list1 to the merged list
            current.next = l1
            # move to the next node in list1
            l1 = l1.next
        else:
            # add the current node from list2 to the merged list
            current.next = l2
            # move to the next node in list2
            l2 = l2.next
        # move the pointer to the next node in the merged list
        current = current.next

    # add any remaining nodes from list1 or list2 to the merged list
    if l1:
        current.next = l1
    if l2:
        current.next = l2

    # return the head of the merged list (i.e., the next node after the dummy node)
    return dummy.next
# create the first linked list: 1 -> 2 -> 4
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# create the second linked list: 1 -> 3 -> 4
list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

# merge the two linked lists
merged_list = mergeTwoLists(list1, list2)

# print the values of the nodes in the merged list: 1 -> 1 -> 2 -> 3 -> 4 -> 4
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
