# Kids with the Greatest Number of Candies

# There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

# Note that multiple kids can have the greatest number of candies.

class Solution(object):
    def kids_with_candies(self, candies, extra_candies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_val = 0
        return_arr = [True] * len(candies)

        for candy in candies:
            if candy > max_val:
                max_val = candy

        for i in range(len(candies)):
            if not candies[i] + extra_candies >= max_val:
                return_arr[i] = False
        
        return return_arr
    
if __name__ == "__main__":
    sol = Solution()
    candies = [4, 2, 1, 1, 2]
    extra_candies = 1
    print(sol.kids_with_candies(candies, extra_candies))