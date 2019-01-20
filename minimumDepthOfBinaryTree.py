class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # bfs with iterative approach, stack
        if root is None:
            return 0
        stack = [root]
        depth = 0
        while stack:
            depth += 1
            nextLevel = []
            for node in stack:       
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            stack = nextLevel
        return depth
    