class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for n in range(len(nums)):

            compli = target - nums[n]

            if compli in prevMap:
                return [prevMap[compli], n]
            prevMap[nums[n]] = n
        return []