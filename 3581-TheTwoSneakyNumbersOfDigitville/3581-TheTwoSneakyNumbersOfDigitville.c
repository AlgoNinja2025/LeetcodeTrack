// Last updated: 7/21/2026, 7:07:23 PM
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getSneakyNumbers(int* nums, int numsSize, int* returnSize) {
   int* result=(int *)malloc(2 *sizeof(int)),n=0;
    for(int i=0;i<numsSize;i++)
    for(int j=i+1;j<numsSize;j++)
    {
        if(nums[j]==nums[i])
        {
            result[n]=nums[j];
            n+=1;
            *returnSize=2;
        }
    }
    return result;
}