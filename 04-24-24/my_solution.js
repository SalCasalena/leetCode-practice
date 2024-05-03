var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
function twoSum(nums, target) {
    var indexes = [];
    var sorted_array = __spreadArray([], nums, true).sort(function (a, b) { return a - b; });
    console.log("Sorted", sorted_array);
    var i = 0;
    while (sorted_array[i] < target) {
        var j = 0;
        while (sorted_array[j] < target) {
            console.log("i:".concat(i, ", j:").concat(j));
            if ((sorted_array[i] + sorted_array[j]) === target) {
                indexes.push(nums.indexOf(sorted_array[i]), nums.indexOf(sorted_array[j]));
                return indexes;
            }
            j++;
        }
        i++;
    }
    return indexes;
}
;
console.log(twoSum([3, 2, 4], 6));
