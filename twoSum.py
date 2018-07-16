class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary = {}
        for i, number in enumerate(nums):
            comp = target - nums[i]
            if (dictionary.get(comp) != None):
                return dictionary[comp], i
            dictionary[nums[i]] = i