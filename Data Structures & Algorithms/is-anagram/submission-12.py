class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
        
        for j in range(len(t)):
            countT[t[j]] = 1 + countT.get(t[j], 0)
        
        # Had made a mistake, where I did `countS[i]`,
        # instead of `countS[s[i]]`
        # print(countS)
        # print(countT)
        return countS == countT
        