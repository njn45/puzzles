"""
Given a string s, return the longest palindromic substring in s.

A string is called a palindrome string if the reverse of that string is the same as the original string.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""

class Solution:

    def longest_palindrome(s:str) -> str: # probably the best any normal person could come up with O(n^2)
        pass
                    
                

    
def main():
    assert Solution.longest_palindrome("babad") in ["bab", "aba"]
    assert Solution.longest_palindrome("cbbd") == "bb"
    assert Solution.longest_palindrome("hellonumber47") == "ll"
    assert Solution.longest_palindrome("1110001101010111101010101010101010") in ["10101010101010101","01010101010101010"]
    assert Solution.longest_palindrome("") == ""
    assert Solution.longest_palindrome("ertyuytrertyutretyui") in ["ertyuytre", "uytrertyu"]
    assert Solution.longest_palindrome("ssssssssss") == "ssssssssss"
    assert Solution.longest_palindrome("mississipi") == "ississi"
    assert Solution.longest_palindrome("4567654565456787656789876544567898765434567898765678765456789876") == "567898765434567898765"
    assert Solution.longest_palindrome("SQQSYYSQQ") == "QQSYYSQQ"

if __name__ == "__main__":
    main()