class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    #  Given a linked list, reverse it iteratively.
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if head is None or head.next is None:
        return head
    prev = None
    curr = head
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev
        
    
def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverse(l)
printll(l)
