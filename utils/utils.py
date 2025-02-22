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


if __name__ == "__main__":
    # Example usage:
    # Constructing a sample tree:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)

    print_tree(root)
