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

    def test_func(input,output):
        input = {tuple(sorted(i)) for i in input}
        output = {tuple(sorted(j)) for j in output}

        return input == output

    assert test_func(Solution.group_anagrams(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]]) == True
    assert test_func(Solution.group_anagrams([""]), [[""]]) == True
    assert test_func(Solution.group_anagrams(["a"]), [["a"]]) == True
    assert test_func(Solution.group_anagrams(["",""]), [["",""]]) == True
    assert test_func(Solution.group_anagrams(["","b"]), [["b"],[""]]) == True
    assert test_func(Solution.group_anagrams(["c","c"]), [["c","c"]]) == True
    assert test_func(Solution.group_anagrams(["ant","ant"]), [["ant","ant"]]) == True
    assert test_func(Solution.group_anagrams(["and","dan"]), [["and","dan"]]) == True
    assert test_func(Solution.group_anagrams(["","b",""]), [["b"],["",""]]) == True
    assert test_func(Solution.group_anagrams(["","",""]), [["","",""]]) == True
    assert test_func(Solution.group_anagrams(["ape","and","cat"]), [["cat"],["and"],["ape"]]) == True
    assert test_func(Solution.group_anagrams(["ape","pea","tax"]), [["tax"],["ape","pea"]]) == True


if __name__ == "__main__":
    main()