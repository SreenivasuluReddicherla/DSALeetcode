class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        if len(t)==0:
            return False
        tr = 0
        for ch in t:
            if tr<len(s) and s[tr]==ch:
                tr+=1
        return tr == len(s)