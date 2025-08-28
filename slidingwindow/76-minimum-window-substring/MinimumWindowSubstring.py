class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        t_count = Counter(t)
        window = {}
        required = len(t_count)
        formed = 0

        l, r = 0, 0
        min_len = float("inf")
        min_window = (0, 0)

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in t_count and window[char] == t_count[char]:
                formed += 1

            while l <= r and formed == required:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l, r)

                left_char = s[l]
                window[left_char] -= 1
                if left_char in t_count and window[left_char] < t_count[left_char]:
                    formed -= 1
                l += 1

            r += 1

        return "" if min_len == float("inf") else s[min_window[0]: min_window[1] + 1]