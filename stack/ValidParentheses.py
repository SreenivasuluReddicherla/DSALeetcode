class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)%2 != 0:
            return False
        for ch in s:
            if ch == '(':
                stack.append(')')
            elif ch == '[':
                stack.append(']')
            elif ch == '{':
                stack.append('}')
            else:
                if not stack or stack.pop()!=ch:
                    return False
        return not stack