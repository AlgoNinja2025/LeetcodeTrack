// Last updated: 7/21/2026, 7:10:26 PM
int removeElement(int* nums, int numsSize, int val) {

    int i;
    int c=0;

    for(i=0;i<numsSize;i++){
        if (nums[i] != val){
            nums[c] = nums[i];
            c++;
        }
    }
   
    return c;
    
}