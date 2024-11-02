
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        
        stack = []
        current_num = 0
        op = '+'

        for i in range(len(s)):
            current_char = s[i]
            
            if current_char.isdigit():
                current_num = (current_num * 10) + int(current_char)

            if (not current_char.isdigit() and not current_char == ' ') or i == n-1:
                if op == '+':
                    stack.append(current_num)
                elif op == '-':
                    stack.append(-1 * current_num)
                elif op == '*':
                    stack.append(stack.pop() * current_num)
                elif op == '/':
                    last_num = stack.pop()
                    # // always is divide with result being floor, so we need consistency between positive and negative results
                    stack.append(last_num // current_num if last_num * current_num >= 0 else -(-last_num // current_num))
                    
                op = current_char
                current_num = 0
                
        return sum(stack)
        
if __name__ == "__main__":
    solution = Solution()
    s = "14-3/2"
    print(solution.calculate(s))