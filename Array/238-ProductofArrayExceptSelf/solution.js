/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
    const n = nums.length;
    const prefixProduct = new Array(n);
    const suffixProduct = new Array(n);
    const result = new Array(n);

    // Calculate prefix products
    prefixProduct[0] = 1;
    for (let i = 1; i < n; i++) {
        prefixProduct[i] = prefixProduct[i - 1] * nums[i - 1];
    }

    // Calculate suffix products
    suffixProduct[n - 1] = 1;
    for (let i = n - 2; i >= 0; i--) {
        suffixProduct[i] = suffixProduct[i + 1] * nums[i + 1];
    }

    // Calculate the product except self
    for (let i = 0; i < n; i++) {
        result[i] = prefixProduct[i] * suffixProduct[i];
    }

    console.log(result);
    return result;
};