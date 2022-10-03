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
        """ Idea is to expand outwards, so each character is the middle of a palindrome"""

        if not s: return ""
        
        result, result_len = "", 0
        # find longest odd length palindrome
        for idx in range(len(s)):
            left, right = idx, idx # two pointers
            
            while left >= 0 and right < len(s) and s[left] == s[right]: # while left and right pointers are in-bounds and we have a palindrome
                
                if (right - left) + 1 > result_len: # we've found a new longest palindrome
                    
                    result, result_len = s[left:right+1], (right - left) + 1 # update what our palindrome is and its length

                left, right = left - 1, right + 1 # seek outwards from the current character
        
        # find longest even length palindrome
        for idx in range(len(s)):
            left, right = idx, idx + 1 # two pointers but the right is offest by 1, to allow for searching palindromes of even length
            
            while left >= 0 and right < len(s) and s[left] == s[right]: # while left and right pointers are in-bounds and we have a palindrome
                
                if (right - left) + 1 > result_len: # we've found a new longest palindrome
                    
                    result, result_len = s[left:right+1], (right - left) + 1 # update what our palindrome is and its length

                left, right = left - 1, right + 1 # seek outwards from the current character
        
        return result


    def manachers_algorithm(s:str) -> str: # O(n)
        
        if not s: return ""

        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join(f'^{s}$')
        n = len(T)
        P = [0] * n
        C = R = 0 # Center and Right
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

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