class NumberContainers {
private indexMap: Map<number, number>;
    private numberMap: Map<number, { heap: number[], set: Set<number> }>;

    constructor() {
        this.indexMap = new Map();
        this.numberMap = new Map();
    }

    change(index: number, number: number): void {
        const oldNumber = this.indexMap.get(index);
        if (oldNumber !== undefined) {
            const oldEntry = this.numberMap.get(oldNumber);
            if (oldEntry) {
                oldEntry.set.delete(index);
            }
        }

        this.indexMap.set(index, number);

        let entry = this.numberMap.get(number);
        if (!entry) {
            entry = { heap: [], set: new Set() };
            this.numberMap.set(number, entry);
        }

        if (!entry.set.has(index)) {
            this.heapInsert(entry.heap, index);
            entry.set.add(index);
        }
    }

    find(number: number): number {
        const entry = this.numberMap.get(number);
        if (!entry) return -1;

        const { heap, set } = entry;
        while (heap.length > 0) {
            const minIndex = this.heapPeek(heap);
            if (set.has(minIndex)) {
                return minIndex;
            } else {
                this.heapExtractMin(heap);
            }
        }

        return -1;
    }

    private heapInsert(heap: number[], value: number): void {
        heap.push(value);
        let i = heap.length - 1;
        while (i > 0) {
            const parent = Math.floor((i - 1) / 2);
            if (heap[i] >= heap[parent]) break;
            [heap[i], heap[parent]] = [heap[parent], heap[i]];
            i = parent;
        }
    }

    private heapExtractMin(heap: number[]): number | undefined {
        if (heap.length === 0) return undefined;
        const min = heap[0];
        const last = heap.pop()!;
        if (heap.length > 0) {
            heap[0] = last;
            let i = 0;
            while (true) {
                const left = 2 * i + 1;
                const right = 2 * i + 2;
                let smallest = i;
                if (left < heap.length && heap[left] < heap[smallest]) {
                    smallest = left;
                }
                if (right < heap.length && heap[right] < heap[smallest]) {
                    smallest = right;
                }
                if (smallest === i) break;
                [heap[i], heap[smallest]] = [heap[smallest], heap[i]];
                i = smallest;
            }
        }
        return min;
    }

    private heapPeek(heap: number[]): number {
        return heap[0];
    }
}

/**
 * Your NumberContainers object will be instantiated and called as such:
 * var obj = new NumberContainers()
 * obj.change(index,number)
 * var param_2 = obj.find(number)
 */