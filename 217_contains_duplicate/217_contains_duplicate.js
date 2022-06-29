/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var containsDuplicate = function(nums) {
    let duplicate = new Set([]);
    for (let i = 0; i < nums.length; i++) {
        if (duplicate.has(nums[i])) return true
        duplicate.add(nums[i])
    }    
    return false
};

let nums = [1,1,1,3,3,4,3,2,4,2];


console.log(containsDuplicate(nums));