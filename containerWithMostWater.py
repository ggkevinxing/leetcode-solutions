# two pointers, iterate pointers when opposite pointer is at higher height
# keep taking area along the way at each step, replacing maxArea if greater
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        currArea = 0
        maxArea = currArea
        left = 0
        right = len(height)-1
        while left < right:
            hL = height[left]
            hR = height[right]
            width = right - left
            if hL < hR:
                currArea = width * hL
                while height[left] <= hL and left < len(height):
                    left += 1
            else:
                currArea = width * hR
                while height[right] <= hR and right >= 0:
                    right -= 1
            maxArea = max(maxArea, currArea)
        return maxArea