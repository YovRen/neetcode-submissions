class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = "".join([ss for ss in s.lower() if ss.isalnum()])
        return s_==s_[::-1]
        