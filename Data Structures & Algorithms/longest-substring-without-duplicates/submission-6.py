class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevSeen = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in prevSeen:
                prevSeen.remove(s[l])
                l += 1
            prevSeen.add(s[r])
            res = max(res, r - l + 1)
        return res