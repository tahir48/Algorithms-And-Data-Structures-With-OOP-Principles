import { TouchableHighlightBase } from "react-native"

export class Graph {
    constructor(){
        this.adjacency_list = {}
    }


    print_graph(){
        for (var vertex in this.adjacency_list){
            console.log(vertex, ":", this.adjacency_list[vertex])
        }
    }

    add_vertex(vertex){
        if (!(vertex in this.adjacency_list)) {
            this.adjacency_list[vertex] = []
            return true
        }
        return false
    }

    add_edge(vertex1,vertex2){
        if (!(vertex2 in this.adjacency_list[vertex1]) && !(vertex1 in this.adjacency_list[vertex2])) {
            this.adjacency_list[vertex1].push(vertex2);
            this.adjacency_list[vertex2].push(vertex1)
        } else {
            return false
        }

    }

    remove_edge(vertex1,vertex2) {
        if (!(vertex2 in this.adjacency_list[vertex1]) && !(vertex1 in this.adjacency_list[vertex2])) {
            const index1 = this.adjacency_list[vertex1].indexOf(vertex2);
            const index2 = this.adjacency_list[vertex2].indexOf(vertex1);

            this.adjacency_list[vertex1].splice(index1,1)
            this.adjacency_list[vertex2].splice(index2,1)

        } else {
            return false
        }
    }





}