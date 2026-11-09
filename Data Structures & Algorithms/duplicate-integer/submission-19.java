class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> prevSeen = new HashSet<Integer>();

        for(int i = 0; i < nums.length; i++) {
            if(prevSeen.contains(nums[i])){
                return true;
            }
            else {
                prevSeen.add(nums[i]);
            }
        }
        
        return false;
    }
}