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
from collections import defaultdict,Counter
class Solution:
    
    def is_anagram(s1:str,s2:str) -> bool:
        if len(s1) != len(s2): return False

        s1_count, s2_count = defaultdict(int), defaultdict(int)
        for idx in range(len(s1)): # count all the characters in each string
            s1_count[s1[idx]] += 1
            s2_count[s2[idx]] += 1
        
        return s1_count == s2_count
    
    def builtin_is_anagram(s1:str,s2:str)->bool:
        if len(s1) != len(s2): return False

        return Counter(s1) == Counter(s2)

def main():
    assert Solution.is_anagram("anagram","nagaram") == True
    assert Solution.is_anagram("rat","car") == False
    assert Solution.is_anagram("orchestra","carthorse") == True
    assert Solution.is_anagram("((]])()","[[[))((") == False
    assert Solution.is_anagram("abcdefghijklmnopqrstuvwxyz","zyxwvutsrpomnlkjihgfedcba") == False
    assert Solution.is_anagram("😀😃😄😁","😁😄😀😃") == True

if __name__ == "__main__":
    main()