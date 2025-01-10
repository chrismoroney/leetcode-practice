# Container with Most Water

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution(object):
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            l = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, l * h)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
    
if __name__ == "__main__":
    sol = Solution()
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(sol.max_area(heights))