class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def getNext(n):
            total = 0
            while n>0:
                digit = n%10
                total += digit*digit
                n//=10
            return total
        while n!=1 and n not in seen:
            seen.add(n)
            n = getNext(n)
        return n==1