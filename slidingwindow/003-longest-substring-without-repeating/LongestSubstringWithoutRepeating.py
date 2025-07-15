class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start =0
        maxLen =0
        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]]>=start:
                start = char_index[s[end]]+1
            char_index[s[end]]=end
            maxLen = max(maxLen, end-start+1)
        return maxLen