function clearDigits(s: string): string {
    let newString: string[] = [];
    s.split("").map((char, index) => {
        if (/\d/.test(char)) {
            if (newString.length > 0 && !/\d/.test(newString[newString.length - 1])) {
                newString.pop();
            }
        } else {
            newString.push(char);
        }
    })

    return newString.join("");
};