"""
Write a function to find the longest common prefix string amongst an array of strings.
The prefix must be present in all input strings to be considered "common"

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Example 3:

Input: strs = ["dog","dodge","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.

"""

class Solution:

    def longest_common_prefix(strs:list[str]) -> str:
        if not strs: return ""
        
        prefix = min(strs, key = len) # because all strings have to share a prefix we can start with the shortest
        for txt in strs:
            while prefix != txt[:len(prefix)]: # check if the current entire prefix matches 
                prefix = prefix[:-1]
        return prefix

def main():
    assert Solution.longest_common_prefix(["flower","flow","flight"]) == "fl"
    assert Solution.longest_common_prefix(["dog","racecar","car"]) == ""
    assert Solution.longest_common_prefix(["dog","dodge","car"]) == ""
    assert Solution.longest_common_prefix([]) == ""
    assert Solution.longest_common_prefix(["abcdefgskljflskdjf","abcdeskjdlksjf","abcdskjfiehsqoiqjwksjlks"]) == "abcd"
    assert Solution.longest_common_prefix(["anticlimax","antiaircraft","antiseptic","antibody"]) == "anti"
    assert Solution.longest_common_prefix(["devalue","deactivate","debug","degrade","deduce"]) == "de"
    assert Solution.longest_common_prefix([""]) == ""

if __name__ == "__main__":
    main()