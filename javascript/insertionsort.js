import { switch_elements } from "./switch_elements.js";



export function insertion_sort(unsorted_list){
    for (var i = 0; i < unsorted_list.length; i++ ) {
        var t = i,
            j = i-1,
            temp = unsorted_list[i];
            while (temp < unsorted_list[j] && j > -1) {
                if (unsorted_list[j] > temp) {
                    switch_elements(unsorted_list,t,j);
                    j -= 1;
                    t -= 1;
                }

            }
    
    }
return unsorted_list
}