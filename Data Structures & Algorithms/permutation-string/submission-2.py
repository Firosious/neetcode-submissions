class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1Count, window = [0] * 26, [0] * 26
        matches = 0

        # initialising hashmaps
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        if s1Count == window:
            return True
        
        l = 0

        # sliding window
        for r in range(len(s1), len(s2)):
            window[ord(s2[r]) - ord('a')] += 1
            window[ord(s2[l]) - ord('a')] -= 1
            
            l += 1
            if s1Count == window:
                return True
        return False
