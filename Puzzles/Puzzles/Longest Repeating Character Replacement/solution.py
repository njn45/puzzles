"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
Or replace the one 'B' and replace with an 'A' -> "AAAABBA"

 

Constraints:

    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length

"""
from collections import defaultdict
class Solution:

    def character_replacement(s: str, k: int) -> int:
        """
        Make a sliding window. The key bit of insight here is keep to track of the most common letter in the window and the size of the window. 
        If size_of_window - most_common_letter_count > k its not valid. 
        size_of_window - most_common_letter_count calculates how many letters would need to be swapped.
        """
        count, result = defaultdict(int), 0

        left, max_freq = 0, 0
        for right in range(len(s)):
            
            count[s[right]] += 1 # look up the character we are on and increase its count by 1
            max_freq = max(max_freq, count[s[right]]) # if we keep track of the current max_frequency like this we dont have to iterate through the values of our count_dict

            if right - left + 1 - max_freq > k: # sliding window is not valid, "right - left + 1 - max_freq" indicates how many letters would need to be swapped
                count[s[left]] -= 1
                left += 1 # move the left side of the window forward

            else: # window is valid
                result = max(result, right - left + 1) # max(current result, size of sliding window)
        
        return result


def main():
    assert Solution.character_replacement("ABAB",2) == 4
    assert Solution.character_replacement("AABABBA",1) == 4
    assert Solution.character_replacement('RVLXSMBRQGTTQFVIPNFPKOOKUUQDICTBAYVBZ',5) == 7
    assert Solution.character_replacement('CEAEFFDAEBDDABC',3) == 6
    assert Solution.character_replacement('KGKFHJKILIIGFHFLGGJILJKKHFLIFFKGHHGHKHJFKKHJJIJIHKJF',8) == 13
    assert Solution.character_replacement("A",1) == 1

if __name__ == "__main__":
    main()