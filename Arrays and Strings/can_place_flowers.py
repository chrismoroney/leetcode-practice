# Can Place Flowers

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, 
# return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class Solution(object):
    def can_place_flowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        extra_flowers = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i-1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if left_empty and right_empty:
                    extra_flowers += 1
                    flowerbed[i] = 1
                    if extra_flowers >= n:
                        return True

        return extra_flowers >= n
    
if __name__ == "__main__":
    sol = Solution()
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(sol.can_place_flowers(flowerbed, n))