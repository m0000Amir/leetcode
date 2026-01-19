# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []

        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left  # 1, 2, 4
            curr = stack.pop()  # 4
            result.append(curr.val)
            curr = curr.right
        return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()
    print(solution.inorderTraversal(root))
