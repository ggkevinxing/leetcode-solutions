class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1 += nums2
        nums1.sort()
        listLen = len(nums1)
        middleInd = (listLen - 1) // 2
        if listLen % 2 == 1:
            return nums1[middleInd]
        else:
            return (nums1[middleInd] + nums1[middleInd + 1]) / 2
        