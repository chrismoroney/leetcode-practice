# Find the Highest Altitude

# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. 
# The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). 
# Return the highest altitude of a point.

class Solution(object):
    def largest_altitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        prefix_sum = [0] * (len(gain) + 1)

        for i in range(len(gain)):
            prefix_sum[i+1] = prefix_sum[i] + gain[i]

        max_altitude = prefix_sum[0]
        for i in range(1, len(prefix_sum)):
            max_altitude = max(max_altitude, prefix_sum[i])
        
        return max_altitude
    
if __name__ == "__main__":
    sol = Solution()
    gain = [-5,1,5,0,-7]
    gain2 = [-4,-3,-2,-1,4,3,2]
    print(sol.largest_altitude(gain))
    print(sol.largest_altitude(gain2))