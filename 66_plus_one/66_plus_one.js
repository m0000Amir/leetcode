/**
 * @param {number[]} digits
 * @return {number[]}
 */
 var plusOne = function(digits) {
    //  1 method
    // return [...String((Number(digits.join('')) + 1))].map(Number);

    // 2 method

    if (digits[digits.length-1] !== 9) {
        digits[digits.length-1] += 1;
        return digits;
    } else {
        digits = [0, ...digits];
 
        for (let i = digits.length-1; i >= 0; --i) {
            if (digits[i] === 9) {
                digits[i] = 0;
            } else {
                digits[i] = digits[i] + 1;
                break
            }
        }
    }
    return digits[0] === 0 ? digits.slice(1) : digits.slice(0)
};

const digits = [6,1,4,5,3,9,0,1,9,5,1,8,6,7,0,5,5,4,3];
console.log(plusOne(digits));
