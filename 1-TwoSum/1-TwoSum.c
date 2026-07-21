// Last updated: 7/21/2026, 7:10:56 PM
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
   int i;
    for(i = 0; i < numsSize; i++) {  
        for(int j = i + 1; j < numsSize; j++) {  
            if(nums[j] == target - nums[i]) {
                int* result = (int*)malloc(sizeof(int) * 2);
                if (result == NULL) {  
                    *returnSize = 0;
                    return NULL;
                }
                result[0] = i;
                result[1] = j;
                *returnSize = 2;
                return result;
            }
        }
    }
    *returnSize = 0;
    return NULL;
}