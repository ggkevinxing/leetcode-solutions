from collections import defaultdict
class Solution(object):
    def threeSum_twoSum_style(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        nums.sort()
        for i in range(0, len(nums) - 1):
            # duplicate case
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            
            # with fixed first number at nums[i], solve like 2sum with compliments
            twoSumSet = set()
            j = i+1
            while j < len(nums):
                compliment = -nums[i] - nums[j]
                if compliment in twoSumSet:
                    res.append(sorted([nums[i], compliment, nums[j]]))
                    # duplicate case, optimization to help avoid TLE error
                    while j < len(nums) -1 and nums[j] == nums[j+1]:
                        j += 1
                else:
                    twoSumSet.add(nums[j])
                j += 1
        
        return res

    def threeSum_with_positive_negative_lists(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = []
        numCounts = defaultdict(int)
        for num in nums:
            numCounts[num] += 1
        if numCounts[0] >= 3:
            res.append([0,0,0])
        positives = []
        negatives = []
        for k,v in numCounts.iteritems():
            if v > 0:
                if k > 0:
                    positives.append(k)
                if k < 0:
                    negatives.append(k)
        negatives.sort()
        for p in positives:
            for n in negatives:
                comp = -p-n
                if comp in numCounts and numCounts[comp] > 0:
                    # if compliment is one of the two values we have to make sure we have seen at least two of that value
                    if (comp == p or comp == n) and numCounts[comp] >= 2:
                        res.append([n, comp, p])
                    elif n < comp < p:
                        res.append([n, comp, p])
                    if comp < n:
                        break
        return res