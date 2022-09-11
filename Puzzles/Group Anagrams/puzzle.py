"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:

Input: strs = [""]
Output: [[""]]

Example 3:

Input: strs = ["a"]
Output: [["a"]]

 

Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.

"""

class Solution:

    def group_anagrams(strs: list[str]) -> list[list[str]]:
        pass

def main():
    assert sorted(Solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]), key = len) == [["bat"],["nat","tan"],["ate","eat","tea"]]
    assert sorted(Solution.group_anagrams([""]), key = len) == [[""]]
    assert sorted(Solution.group_anagrams(["a"]), key = len) == [["a"]]
    assert sorted(Solution.group_anagrams(["",""]), key = len) == [["",""]]
    assert sorted(Solution.group_anagrams(["","b"]), key = len) == [["b"],[""]]
    assert sorted(Solution.group_anagrams(["c","c"]), key = len) == [["c","c"]]
    assert sorted(Solution.group_anagrams(["ant","ant"]), key = len) == [["ant","ant"]]
    assert sorted(Solution.group_anagrams(["and","dan"]), key = len) == [["and","dan"]]
    assert sorted(Solution.group_anagrams(["","b",""]), key = len) == [["b"],["",""]]
    assert sorted(Solution.group_anagrams(["","",""]), key = len) == [["","",""]]
    assert sorted(Solution.group_anagrams(["ape","and","cat"]), key = len) == [["cat"],["and"],["ape"]]
    assert sorted(Solution.group_anagrams(["ape","pea","tax"]), key = len) == [["tax"],["ape","pea"]]


if __name__ == "__main__":
    main()