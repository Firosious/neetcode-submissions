class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            if (map.containsKey(target - nums[i])) {
                return new int[] { map.get(target - nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }
}

// - Time Complexity = O(n), where n is the length of the input array
//      - O(n), visit each index once
// - Space Complexity = O(n), where n is the length of the input array
//      - O(n), map