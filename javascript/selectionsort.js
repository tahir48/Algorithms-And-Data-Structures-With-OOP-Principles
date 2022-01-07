import { switch_elements } from "./switch_elements.js";



export function selection_sort(unsorted_list){
    for (var i = 0; i < unsorted_list.length; i++ ) {
        for (var j = i+1; j <= unsorted_list.length; j++) {
            if(unsorted_list[j] < unsorted_list[i]){
                switch_elements(unsorted_list,j,i)
            }
        }
    }
    return unsorted_list
}







// from bubblesort import switch

// #first item is minimum at first iteration is guaranteed


// def selection_sort(unsorted_list):
//     for i in range(len(unsorted_list)): # i is my min index
//         for j in range(i+1, len(unsorted_list)):
//             if unsorted_list[j] < unsorted_list[i]:
//                 switch(unsorted_list,j,i)
//     return unsorted_list


