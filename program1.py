class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in bracket_map:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Pop from stack or use dummy value
                if bracket_map[char] != top_element:
                    return False
            else:  # If it's an opening bracket
                stack.append(char)

        return not stack  # If stack is empty, return True; otherwise, False
