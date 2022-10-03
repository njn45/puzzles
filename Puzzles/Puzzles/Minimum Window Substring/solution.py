"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

 

Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.

 

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""
from collections import defaultdict as d, Counter
class Solution:
    def min_window(s: str, t: str) -> str:
        """sliding window
        move forward with the right pointer when you dont have a valid solution.
        once you've got a valid solution, keep track of its indexes and its length.
        then start moving forward with the left pointer until the solution is no longer valid
        each time you get a new solution, compare its length"""
        if not t or len(t) > len(s): return ''

        t = Counter(t)
        window = d(int)

        current_chars, need_chars = 0, len(t)
        result, result_length = [-1,-1], len(s) + 1

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in t and window[c] == t[c]: #if character is in the target and their counts are the same
                current_chars += 1
            
            while current_chars == need_chars: # we have a solution
                if r - l + 1 < result_length: # if size of window < current result
                    result, result_length = [l,r], r - l + 1 # update our results
                
                # start making the window smaller
                c = s[l] # override the character we're looking at from the right idx to the left idx
                window[c] -= 1 # decrement how many times we've seen the leftmost character
                if c in t and window[c] < t[c]: # check if our window is still a valid solution
                    current_chars -= 1 # not a valid solution
                
                l += 1

        l, r = result
        return s[l:r+1] if result_length < len(s) + 1 else ''




def main():
    assert Solution.min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert Solution.min_window("a", "a") == "a"
    assert Solution.min_window("a", "aa") == ""
    assert Solution.min_window("a", "") == ""
    assert Solution.min_window("a", "b") == ""
    assert Solution.min_window("ab", "a") == "a"
    assert Solution.min_window("ab", "b") == "b"
    assert Solution.min_window("ab", "A") == ""
    assert Solution.min_window("ab", "B") == ""
    assert Solution.min_window("SUPERCALIFRAGILISTICEXPIALIDOCIOUS", "GLIS") == "GILIS"

if __name__ == "__main__":
    main()