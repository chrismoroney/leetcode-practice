# Asteroid Collision

# We are given an array asteroids of integers representing asteroids in a row. 
# The indices of the asteriod in the array represent their relative position in space.

# For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. 
# If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

class Solution(object):
    def asteroid_collision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []
        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                top = stack.pop()
                if abs(top) == abs(a):
                    a = 0
                    break
                elif abs(top) > abs(a):
                    a = top
            if a:
                stack.append(a)
        
        return stack
    
if __name__ == "__main__":
    sol = Solution()
    asteroids = [5, 10, -5]
    print(sol.asteroid_collision(asteroids))