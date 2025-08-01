class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        stot = {}
        ttos = {}
        for sc, tc in zip(s, t):
            if sc in stot:
                if stot[sc]!=tc:
                    return False
            else:
                stot[sc]=tc
            if tc in ttos:
                if ttos[tc]!=sc:
                    return False
            else:
                ttos[tc]=sc
        return True
