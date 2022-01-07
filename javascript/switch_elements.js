export function switch_elements(list,index1,index2) {
    temp = list[index1];
    list[index1] = list[index2];
    list[index2] = temp;
    return list
}
