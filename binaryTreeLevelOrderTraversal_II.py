class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            toAdd = []
            for node in stack:
                toAdd.append(node.val)
            result.insert(0, toAdd)
            nextLevel = []
            for node in stack:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            stack = nextLevel
        return result