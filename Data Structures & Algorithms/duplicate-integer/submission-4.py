class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duped = set()

        for i in nums:
            if i in duped:
                return True
            else:
                duped.add(i)
        return False