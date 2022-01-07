import { TreeNode } from "./mynodes.js";



export class BinarySearchTree {
    constructor(value){
        var newnode = new TreeNode(value);
        this.root = newnode
    }


    insert(value){
        var newnode = new TreeNode(value);
        if (this.root == null){
            this.root = newnode;
            return
        }
        temp = this.root;
        while(true){
            if (newnode.value > temp.value){
                if (temp.right != null) {
                    temp = temp.right
                } else {
                    temp.right = newnode;
                    return
                }
            } else {
                if (temp.left != null) {
                    temp = temp.left
                } else {
                    temp.left = newnode;
                    return
                }
            }
        }

    }




    contains(value){
        if (this.root == null){
            return false
        }
        temp = this.root
        while (temp) {
            if(temp.value == value){
                return true
            }
            if (temp.value < value) {
                if(temp.right != null){
                    temp = temp.right
                } else {return false}
            } else if (temp.value > value) {
                if (temp.left != null){
                    temp = temp.left
                } else {return false}
            }
        }
        return false
    }


}

                
