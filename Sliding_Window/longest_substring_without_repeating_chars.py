#Description: Given a string, find the length of the longest substring without repeating characters.

def longest_substring(s: str)-> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    input = ''
    print(longest_substring(input))
