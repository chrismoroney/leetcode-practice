'''
Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

'''

class Solution:
    def reverse_vowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        i = 0
        j = len(s) - 1

        s_list = list(s)

        while i < j:
            while i < len(s_list) and s_list[i] not in vowels:
                i += 1
            
            while j >= 0 and s_list[j] not in vowels:
                j -= 1

            if i < j:
                s_list[i], s_list[j] = s_list[j], s_list[i]
                i += 1
                j -= 1
        
        return ''.join(s_list)
    
if __name__ == "__main__":
    sol = Solution()
    s = "AntIdisestablIshmEntarIAnIsm"
    print(sol.reverse_vowels(s))
