# Integer to English Words

# Convert a non-negative integer num to its English words representation.

class Solution(object):
    # defaulted arrays, base cases to endpoint with recursion
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    ten_plus_ones = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    ten_to_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    # main call
    def number_to_words(self, num):
        """
        :type num: int
        :rtype: str
        """

        if num == 0:
            return "Zero"

        return self.convert_nums(num)

    # recursive function
    def convert_nums(self, num):
        if num < 10:
            return self.ones[num]
        if num < 20:
            return self.ten_plus_ones[num - 10]
        if num < 100:
            return self.ten_to_hundred[num // 10] + (" " + self.convert_nums(num % 10) if num % 10 != 0 else "")
        
        if num < 1000:
            return self.convert_nums(num // 100) + " Hundred" + (" " + self.convert_nums(num % 100) if num % 100 != 0 else "")

        if num < 1000000:
            return self.convert_nums(num // 1000) + " Thousand" + (" " + self.convert_nums(num % 1000) if num % 1000 != 0 else "")
        
        if num < 1000000000:
            return self.convert_nums(num // 1000000) + " Million" + (" " + self.convert_nums(num % 1000000) if num % 1000000 != 0 else "")

        return self.convert_nums(num // 1000000000) + " Billion" + (" " + self.convert_nums(num % 1000000000) if num % 1000000000 != 0 else "")


if __name__ == "__main__":
    num = 1234567899
    num2 = 83
    sol = Solution()
    print(sol.number_to_words(num))
    print(sol.number_to_words(num2))