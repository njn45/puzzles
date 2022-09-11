"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

EXAMPLES:
1.
Input: s = "()"
Output: true

2.
Input: s = "()[]{}"
Output: true

3.
Input: s = "(]"
Output: false
"""
class Solution:
    
    def is_valid(s:str) -> bool:
        if len(s) & 1: # It is impossible for any odd length strings to be valid
            return False

        lookup, stack = {'(':')', '{':'}','[':']'}, []
        for bracket in s:
            if bracket in lookup: # if a character is in the dict we know it is an open bracket so we add it to the stack
                stack.append(bracket)
            elif not len(stack) or lookup[stack.pop()] != bracket: # If the stack is empty and its a closing bracket it cant be valid or the last element of the stack is not a valid opening bracket
                return False
            
        return not len(stack) # If the stack is empty, everyting is valid, if the stack is not empty the input is invalid

def main():

    assert Solution.is_valid("()") == True
    assert Solution.is_valid("((") == False
    assert Solution.is_valid("())") == False
    assert Solution.is_valid(")()(") == False
    assert Solution.is_valid("()[]{}") == True
    assert Solution.is_valid("(]") == False
    assert Solution.is_valid("([)]") == False
    assert Solution.is_valid("{()}") == True
    assert Solution.is_valid("{([]})") == False

if __name__ == "__main__":
    main()