class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in range(len(nums)):
            if nums[n] in seen:
                return True
            seen.add(nums[n])
        return False