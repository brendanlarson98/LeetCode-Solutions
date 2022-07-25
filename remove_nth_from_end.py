# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = [1,2]
n = 2
head_node = ListNode()
current_node = head_node
for i in range(len(head)):
    new_node = ListNode(head[i])
    current_node.next = new_node
    current_node = new_node


def print_list(node):
    if node:
        print(node.val)
        print_list(node.next)
    else:
        return

def removeNthFromEnd(head, n):
    if not head.next:
        return None
    
    def parse(node, leng):
        if not node:
            return leng
        return parse(node.next, leng+1)

    def count_to_remove_nth(node, count):
        if count == num-n:
            node.next = node.next.next
        else:
            if node.next:
                count_to_remove_nth(node.next, count+1)
            return
        
    num = parse(head, 0)
    if num == n:
        return head.next
                
    count_to_remove_nth(head, 1)
    return head
