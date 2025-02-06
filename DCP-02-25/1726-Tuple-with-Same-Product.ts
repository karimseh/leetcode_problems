function tupleSameProduct(nums: number[]): number {
    let multiples: { [multiple: number]: number } = {};
    for (let i = 0; i < nums.length; i++) {
        for (let j = i + 1; j < nums.length; j++) {
            let currentMultiple = nums[i] * nums[j];
            multiples[currentMultiple] = (multiples[currentMultiple] || 0) + 1;
        }
    }

    let result = 0;
    for (const count of Object.values(multiples)) {
        if (count >= 2) {
            result += count * (count - 1) * 4;
        }
    }

    return result;


};