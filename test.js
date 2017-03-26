
a = function(list, k){
    subsets = []
    s = []
    if (k <= list.length){
        for (var i=0; i < k -1; i++){
            s.push(i)
        }

        while (true) {
        // int i;
        // find position of item that can be incremented
        for (var i = k - 1; i >= 0 && s[i] == list.length - k + i; i--);
        if (i < 0) {
            break;
        } else {
            s[i]++;                    // increment this item
            for (++i; i < k; i++) {    // fill up remaining items
                s[i] = s[i - 1] + 1;
            }
            subsets.push(getSubset(list, s));
        }
    }
    return subsets
    }
    return 0
}


getSubset = function(input, subset){
    result = []
    for (var i=0; i<subset.length; i++){
        result.push(input[subset[i]]);
    }
    return result
}
console.log(a([0, 1 ,2], 2));
