// Last updated: 7/21/2026, 7:07:13 PM
class Solution {
    public int[] findXSum(int[] nums, int k, int x) {
        int[] freq = new int[51];
        List<Integer> ans = new ArrayList<>();
        
        
        for (int i = 0; i < k; i++) {
            freq[nums[i]]++;
        }
        
        for (int i = 0; i + k <= nums.length; i++) {
            List<int[]> vals = new ArrayList<>();
            for (int v = 1; v <= 50; v++) { 
                if (freq[v] > 0) vals.add(new int[]{v, freq[v]});
            }
            
            
            vals.sort((a, b) -> {
                if (a[1] != b[1]) {
                    return b[1] - a[1]; 
                } else {
                    return b[0] - a[0]; 
                }
            });
            
            int sum = 0;
            for (int j = 0; j < x && j < vals.size(); j++) {
                sum += vals.get(j)[0] * vals.get(j)[1];
            }
            ans.add(sum);
            
            if (i + k < nums.length) {
                freq[nums[i]]--;
                freq[nums[i + k]]++;
            }
        }
        
        
        int[] result = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            result[i] = ans.get(i);
        }
        return result;
    }
}