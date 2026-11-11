class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {}

        for n in range(len(nums)):
            comp = target - nums[n]
            if comp in prevSeen:
                return [prevSeen[comp], n]
            prevSeen[nums[n]] = n
        return []