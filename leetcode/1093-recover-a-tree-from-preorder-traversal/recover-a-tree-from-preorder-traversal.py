# Amir Mukhtarov, mukhtarov.amir.a@gmail.com
# Definition for a binary tree node.
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root: TreeNode):
    if not root:
        print("Tree is empty.")
        return

    queue = deque([root])
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(str(node.val) if node else "None")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        print(" ".join(current_level))


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0
        n = len(traversal)

        while index < n:
            depth = 0
            while (index < n) and (traversal[index] == '-'):
                depth += 1
                index += 1

            value = 0
            while (index < n) and (traversal[index].isdigit()):
                value = value * 10 + int(traversal[index])
                index += 1

            node = TreeNode(value)

            while len(stack) > depth:
                stack.pop()

            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

            stack.append(node)

        return stack[0]


if __name__ == '__main__':

    traversal = "1-2--3--4-5--6--7"

    s = Solution()

    print_tree(s.recoverFromPreorder(traversal))
