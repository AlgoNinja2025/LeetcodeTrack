// Last updated: 7/21/2026, 7:10:27 PM
int removeDuplicates(int* nums, int numsSize) {

    if(numsSize == 0){
        return 0;
    }

    int k=1;
    for(int i=1;i<numsSize;i++)
    {
        if(nums[i]!=nums[k-1]){
            nums[k]=nums[i];
            k++;
        }
    }
    return k;
}