function queryResults(limit: number, queries: number[][]): number[] {
    const ballColors = new Map<number, number>();
    const colorCounts = new Map<number, number>();
    const result: number[] = [];

    for (const [x, y] of queries) {
        const prevColor = ballColors.get(x);

        if (prevColor !== undefined) {
            const prevCount = colorCounts.get(prevColor)!;
            if (prevCount === 1) {
                colorCounts.delete(prevColor);
            } else {
                colorCounts.set(prevColor, prevCount - 1);
            }
        }

        ballColors.set(x, y);
        const currentYCount = colorCounts.get(y) ?? 0;
        colorCounts.set(y, currentYCount + 1);

        result.push(colorCounts.size);
    }

    return result;
}

