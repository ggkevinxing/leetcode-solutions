class Solution(object):
    def maxSubArray_naive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums and len(nums) < 2:
            return nums[0]

        maxSum = float('-inf')
        for i in range(len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]
                maxSum = max(maxSum, currSum)
        return maxSum

    def maxSubArray_dp_n_space(self, nums):
    	"""
        :type nums: List[int]
        :rtype: int
        """
        if nums and len(nums) < 2:
        	return nums[0]

    	# maxSums is an array of integers representing the maximum sum of the max subarray seen so far up to given index point
    	maxSums = [0] * len(nums)
    	# base case
    	maxSums[0] = nums[0]
    	result = maxSums[0]
    	for i in range(1, len(nums)):
    		maxSums[i] = max(maxSums[i-1] + nums[i], nums[i])
    		result = max(result, maxSums[i])
		return result
    
    def maxSubArray_dp_constant_space(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
   		if nums and len(nums) < 2:
            return nums[0]
        
        currSum = nums[0]
        maxSum = currSum
        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            maxSum = max(maxSum, currSum)
            
        return maxSum

