/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var searchInsert = function(nums, target) {
    let output = 0;
    for (let i=0; i< nums.length; i++) {
        if (nums[i] == target) return i;
        else {
            if (nums[i] > target) return i;
            else output = i+1;
        }
    }
    return output
};

const nums = [1,3,5,6];
const target = 2;

console.log(searchInsert(nums, target));