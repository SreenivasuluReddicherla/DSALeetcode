class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words)!=len(pattern):
            return False
        ptow = {}
        wtop = {}
        for p, w in zip(pattern, words):
            if p in ptow:
                if ptow[p]!=w:
                    return False
            else:
                ptow[p]=w
            if w in wtop:
                if wtop[w]!=p:
                    return False
            else:
                wtop[w]=p
        return True