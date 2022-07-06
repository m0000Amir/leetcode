/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var search = function(nums, target) {
    let l = 0;
    let h = nums.length - 1;
    while (l <= h) {
        let i = Math.floor((l + h) / 2);
        if (nums[i] === target) return i;
        if (nums[i] < target) {
            l = i + 1;
        } else {
            h =  i - 1;
        };
    };
    return -1;
};


let nums = [-1,0,3,5,9,12];
let target = 9;
console.log(search(nums, target));