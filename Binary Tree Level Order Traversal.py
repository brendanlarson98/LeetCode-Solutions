# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Logic: we perform depth first search down each node. Each each node's value into a nest list, with it's index corresponding to the depth of the node.

def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    int_list = []

    def level_order(node, depth=0):
        if not node:
            return 
        if len(int_list) <= depth:
            int_list.append([])
        int_list[depth].append(node.val)

        level_order(node.left, depth+1)
        level_order(node.right, depth+1)

    level_order(root)

    return int_list
