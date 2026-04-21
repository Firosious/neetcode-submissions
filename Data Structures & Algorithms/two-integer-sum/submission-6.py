class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {} # Number : Index
        for i, n in enumerate(nums):
            compli = target - n
            print(prevSeen)
            if compli in prevSeen:
                print(prevSeen[compli])
                print(i)
                return [prevSeen[compli], i]
            prevSeen[n] = i
            print(prevSeen)
        return [] 