# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    visited = []
    def __init__(self, root: Optional[TreeNode]):
        self.visited = []
        queue = []
        if root:
            root.val = 0
        current = root
        queue.append(current)
        while queue:
            current = queue.pop(0)
            if current:
                self.visited.append(current.val)
                if current.left :
                    current.left.val = current.val * 2 + 1
                if current.right :
                    current.right.val = current.val * 2 + 2
                queue.append(current.left)
                queue.append(current.right)
        

    def find(self, target: int) -> bool:
        return target in self.visited
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)