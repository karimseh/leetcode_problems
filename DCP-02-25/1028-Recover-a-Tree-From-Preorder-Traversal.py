# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        index = 0
        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == '-':
                index += 1
                depth += 1
            val = 0
            while index < len(traversal) and traversal[index].isdigit():
                val = val * 10 + int(traversal[index]) # to for the number at the end
                index += 1
            node = TreeNode(val)
            while len(stack) > depth:
                stack.pop()
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
            
            stack.append(node)

        return stack[0]

