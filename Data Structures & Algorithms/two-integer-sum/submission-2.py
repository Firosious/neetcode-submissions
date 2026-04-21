class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : index

        # here, we can use for i, n <- for both the index and number from the nums list
        for i, n in enumerate(nums):
            # n will be he numbers from the list, we'll go through them, and subtract
            # from the target to get a compliment value that we will check if in 'prevMap'
            compli = target - n
            if compli in prevMap:
                # here prevMap[x] -> gives the index that the value is in,
                # while the ', i' gives us the value using 'i' as the index
                return [prevMap[compli], i]
            else:
                prevMap[n] = i
