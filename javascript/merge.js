export function merge(list1, list2){
    var merged_list = [],
        i = 0,
        j = 0;

    while (i < list1.length && j < list2.length) {
        if (list1[i] < list2[j]) {
            merged_list.push(list1[i]);
            i += 1;
        } else {
            merged_list.push(list2[j]);
            j += 1;
        }
    }

    while (i < list1.length) {
        merged_list.push(list1[i]);
        i += 1
    }

    while (j < list2.length) {
        merged_list.push(list2[j]);
        j += 1
    }

    return merged_list
}