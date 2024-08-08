class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def is_sum_tree(self, node):
        return self._is_sum_tree_helper(node) != -1

    def _is_sum_tree_helper(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.data

        left_sum = self._is_sum_tree_helper(node.left)
        right_sum = self._is_sum_tree_helper(node.right)

        if left_sum == -1 or right_sum == -1 or (left_sum + right_sum != node.data):
            return -1

        return left_sum + right_sum + node.data
