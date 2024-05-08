function twoSum(nums: number[], target: number): number[] {

    const indexes: number[] = [];
    const sorted_array: number[] = [...nums].sort((a, b) => a-b);

    console.log("Sorted", sorted_array);

    let i: number = 0;
    while (sorted_array[i] < target) {
        let j: number = 0;
        while (sorted_array[j] < target) {
            console.log(`i:${i}, j:${j}`)
            if ((sorted_array[i] + sorted_array[j]) === target) {
                const a = nums.indexOf(sorted_array[i]);
                nums[a] = sorted_array[i] + 1;
                const b = nums.indexOf(sorted_array[j]);
                indexes.push(a, b);
                return indexes;
            }
            j++;
        }
        i++;
    }

    return indexes;

};

console.log(twoSum([3, 2, 4], 6));


