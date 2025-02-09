function countBadPairs(nums: number[]): number {
    let iHashMap = new Map<number, number>();
    let goodPairCounter: number = 0
    const n = nums.length;
    const TOTAL_PAIRS = n * (n - 1) / 2;
    for (let i = 0; i < n; i++) {
        let oldCounter = iHashMap.get(nums[i] - i);
        if (oldCounter) {
            goodPairCounter += oldCounter

            iHashMap.set(nums[i] - i, oldCounter + 1);
        } else {
            iHashMap.set(nums[i] - i, 1)
        }

    }

    if (iHashMap.size == 1) {
        return 0;
    }
    return TOTAL_PAIRS - goodPairCounter;
};