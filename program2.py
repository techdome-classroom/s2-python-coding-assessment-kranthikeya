class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:  # If the string is empty, return 0
            return 0
        
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        for i in range(len(s) - 1):
            current_value = roman_map[s[i]]
            next_value = roman_map[s[i + 1]]
            
            if current_value < next_value:
                total -= current_value  # Subtraction case (e.g., IV, IX)
            else:
                total += current_value  # Addition case (e.g., VI, XI)

        # Add the value of the last character
        total += roman_map[s[-1]]

        return total
