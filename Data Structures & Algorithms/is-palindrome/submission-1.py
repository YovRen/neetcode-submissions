class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = ""
        for ss in s.lower():
            if ss.isdigit() or ss.isalpha():
                s_+=ss
        return s_=="".join(list(reversed(s_)))
        