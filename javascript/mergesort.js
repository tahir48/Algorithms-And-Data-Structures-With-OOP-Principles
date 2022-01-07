import { merge } from './merge.js'


export function merge_sort(unsorted_list){
    if (unsorted_list.length == 1) {
        return unsorted_list
    }
    var first_half = unsorted_list.slice(0, Math.floor(unsorted_list.length/2));
    var second_half = unsorted_list.slice(Math.floor(unsorted_list.length/2), unsorted_list.length);
    return merge(merge_sort(first_half) , merge_sort(second_half));
}