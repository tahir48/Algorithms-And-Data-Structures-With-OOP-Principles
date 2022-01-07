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






// from bubblesort import switch


// def insertion_sort(unsorted_list):
//     for i in range(1,len(unsorted_list)): # index of value that will be shifted to 
//         t = i
//         j = i-1
//         temp = unsorted_list[i]
//         while temp < unsorted_list[j] and j > -1:
//             if unsorted_list[j] > temp:
//                 switch(unsorted_list,t,j)
//                 j -= 1
//                 t -= 1
//     return unsorted_list


// print(insertion_sort([2,4,1,6,3,5,9,7,8]))
