# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

# You are given the head of a linked list, and an integer k.
# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = [1,2,3,4,5]
k = 2
head_node = ListNode()
current_node = head_node
for i in range(len(head)):
    new_node = ListNode(head[i])
    current_node.next = new_node
    current_node = new_node
head_node = head_node.next

def print_list(node):
    if node:
        print(node.val)
        print_list(node.next)
    else:
        return

def swap_nodes(head, k):
    lis = []
    node = head
    new_node = head
    i = 0
    while node:
        lis.append(node.val)
        node = node.next
    second_k = len(lis) - k
    lis[k-1], lis[second_k] = lis[second_k], lis[k-1]
    while i < len(lis)-1:
        new_node.val = lis[i]
        new_node = new_node.next
        i += 1

    print_list(head)

swap_nodes(head_node, 2)
