"""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 10^4
    s consists of English letters, digits, symbols and spaces.

"""

class Solution:

    def length_of_longest_substring(s:str) -> int:
        pass

def main():
    assert Solution.length_of_longest_substring("abcabcbb") == 3
    assert Solution.length_of_longest_substring("bbbbb") == 1
    assert Solution.length_of_longest_substring("pwwkew") == 3
    assert Solution.length_of_longest_substring("") == 0
    assert Solution.length_of_longest_substring("au") == 2
    assert Solution.length_of_longest_substring("aab") == 2
    assert Solution.length_of_longest_substring("cdd") == 2
    assert Solution.length_of_longest_substring("bdb") == 2
    assert Solution.length_of_longest_substring("bwf") == 3
    assert Solution.length_of_longest_substring("abba") == 2
    assert Solution.length_of_longest_substring("aaca") == 2
    assert Solution.length_of_longest_substring("abcb") == 3
    assert Solution.length_of_longest_substring("brnk") == 4
    assert Solution.length_of_longest_substring("oqgiqhaofm") == 8
    assert Solution.length_of_longest_substring("acrsjhokiv") == 10
    assert Solution.length_of_longest_substring("gjjtbxuvqx") == 7

if __name__ == "__main__":
    main()