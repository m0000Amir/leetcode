from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        if ((root.left.val + root.right.val) == root.val):
            return True
        return False


if __name__ == "__main__":
    root_list = [5, 3, 1]
    tree_node = TreeNode(val=root_list[0])
    tree_node.left = TreeNode(val=root_list[1])
    tree_node.right = TreeNode(val=root_list[1])

    print(Solution().checkTree(tree_node))
