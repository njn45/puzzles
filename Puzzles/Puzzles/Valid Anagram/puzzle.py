"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 10^4
    s and t consist of lowercase characters
"""

class Solution:

    def is_anagram(s1:str,s2:str) -> bool:
        pass

def main():
    assert Solution.is_anagram("anagram","nagaram") == True
    assert Solution.is_anagram("rat","car") == False
    assert Solution.is_anagram("orchestra","carthorse") == True
    assert Solution.is_anagram("((]])()","[[[))((") == False
    assert Solution.is_anagram("abcdefghijklmnopqrstuvwxyz","zyxwvutsrpomnlkjihgfedcba") == False
    assert Solution.is_anagram("😀😃😄😁","😁😄😀😃") == True

if __name__ == "__main__":
    main()