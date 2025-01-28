class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ""
        for i in s.lower():
            if ord('a') <= ord(i) <= ord('z') or ord('0') <= ord(i) <= ord('9'):
                x += i
        return x == x[::-1]