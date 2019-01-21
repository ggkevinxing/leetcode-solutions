class Solution(object):
    def checkPathSum_recursive(self, root, sum, sumSoFar):
        sumSoFar += root.val
        if root.left is None and root.right is None:
            return sum == sumSoFar
        if root.left and root.right:
            return self.checkPathSum_recursive(root.left, sum, sumSoFar) or self.checkPathSum_recursive(root.right, sum, sumSoFar)
        if root.left:
            return self.checkPathSum_recursive(root.left, sum, sumSoFar)
        if root.right:
            return self.checkPathSum_recursive(root.right, sum, sumSoFar)
        
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.checkPathSum_recursive(root, sum, 0)