import { switch_elements } from "./switch_elements.js";


export function bubble_sort(unsorted_list){
    for (var i = unsorted_list.length - 1; i >= 0; i-- ) {
        for (var j = 0; j <= i; j++) {
            if(unsorted_list[j+1] < unsorted_list[j]){
                switch_elements(unsorted_list,j,j+1)
            }
        }
    }
    return unsorted_list
}
