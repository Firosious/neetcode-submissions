class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duped = set()

        for n in nums:
            if n in duped:
                return True
            duped.add(n)
        return False